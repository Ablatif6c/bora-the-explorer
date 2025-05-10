"""Manages the optimization domain and holds points."""

import math
import numpy as np
import torch
from copy import deepcopy
from typing import Dict, List
from warnings import warn
from colorama import Fore
from .util import NotUniqueError, add_samples_to_cache, ensure_rng


def _hashable(x):
    """Ensure that a point is hashable by a python dict."""
    return tuple(map(float, x))


class Space:

    def __init__(
        self,
        pbounds,
        key_order: List[str] = None,
        constraint=None,
        random_state=None,
        allow_duplicate_points=False,
    ):
        self._random_state = ensure_rng(random_state)
        self._allow_duplicate_points = allow_duplicate_points

        self.n_duplicate_points = 0

        # Get the name of the parameters
        self._keys = key_order

        # Create an array with parameters bounds
        self._bounds = np.array(
            [pbounds[key] for key in self._keys],
            dtype=float,
        )

        # preallocated memory for X and Y points
        self._params = np.empty(shape=(0, self.dim))
        self._target = np.empty(shape=(0,))
        self.dtype = float

        # keep track of unique points we have seen so far
        self._cache = {}
        self._hypothesis_tracking = []

        self._constraint = constraint

        if constraint is not None:
            # preallocated memory for constraint fulfillment
            if constraint.lb.size == 1:
                self._constraint_values = np.empty(shape=(0), dtype=float)
            else:
                self._constraint_values = np.empty(
                    shape=(0, constraint.lb.size), dtype=float
                )

    def __contains__(self, x):
        """Check if this parameter has already been registered.

        Returns
        -------
        bool
        """
        return _hashable(x) in self._cache

    def __len__(self):
        """Return number of observations registered.

        Returns
        -------
        int
        """
        assert len(self._params) == len(self._target)
        return len(self._target)

    @property
    def empty(self):
        """Check if anything has been registered.

        Returns
        -------
        bool
        """
        return len(self) == 0

    @property
    def params(self):
        """Get the parameter values registered to this TargetSpace.

        Returns
        -------
        np.ndarray
        """
        return self._params

    @property
    def target(self):
        """Get the target function values registered to this TargetSpace.

        Returns
        -------
        np.ndarray
        """
        return self._target

    @property
    def dim(self):
        """Get the number of parameter names.

        Returns
        -------
        int
        """
        return len(self._keys)

    @property
    def keys(self):
        """Get the keys (or parameter names).

        Returns
        -------
        list of str
        """
        return self._keys

    @property
    def bounds(self):
        """Get the bounds of this TargetSpace.

        Returns
        -------
        np.ndarray
        """
        return self._bounds

    @bounds.setter
    def bounds(self, new_bounds):
        """Set the bounds of this TargetSpace.

        Parameters
        ----------
        new_bounds : np.ndarray
        """
        self._bounds = new_bounds

    @property
    def constraint(self):
        """Get the constraint model.

        Returns
        -------
        ConstraintModel
        """
        return self._constraint

    @property
    def constraint_values(self):
        """Get the constraint values registered to this TargetSpace.

        Returns
        -------
        np.ndarray
        """
        if self._constraint is None:
            raise AttributeError(
                "TargetSpace belongs to an unconstrained optimization",
            )

        return self._constraint_values

    @property
    def mask(self):
        """Return a boolean array of valid points.

        Points are valid if they satisfy both the constraint and boundary
        conditions.

        Returns
        -------
        np.ndarray
        """
        mask = np.ones_like(self.target, dtype=bool)

        # mask points that don't satisfy the constraint
        if self._constraint is not None:
            allowed = self._constraint.allowed(self._constraint_values)
            mask &= allowed

        # # mask points that are outside the bounds
        # if self._bounds is not None:
        #     within_bounds = np.all(
        #         (self._bounds[:, 0] <= self._params)
        #         & (self._params <= self._bounds[:, 1]),
        #         axis=1,
        #     )
        #     mask &= within_bounds

        return mask

    def params_to_array(self, params):
        """Convert a dict representation of parameters into an array version.

        Parameters
        ----------
        params : dict
            a single point, with len(x) == self.dim.

        Returns
        -------
        np.ndarray
            Representation of the parameters as an array.
        """
        if not set(params) == set(self.keys):
            raise ValueError(
                f"Parameters' keys ({sorted(params)}) do "
                + f"not match the expected set of keys ({self.keys})."
            )
        return np.asarray([params[key] for key in self.keys])

    def array_to_params(self, x):
        """Convert an array representation of parameters into a dict version.

        Parameters
        ----------
        x : np.ndarray
            a single point, with len(x) == self.dim.

        Returns
        -------
        dict
            Representation of the parameters as dictionary.
        """
        if not len(x) == len(self.keys):
            raise ValueError(
                f"Size of array ({len(x)}) is different than the "
                + f"expected number of parameters ({len(self.keys)})."
            )
        return dict(zip(self.keys, x))

    def register(self, params, target, constraint_value=None):
        x = self._as_array(params)
        if x in self:
            if self._allow_duplicate_points:
                self.n_duplicate_points = self.n_duplicate_points + 1

                print(
                    Fore.RED
                    + f"Data point {x} is not unique. "
                    + f"{self.n_duplicate_points} duplicates registered. "
                    + "Continuing ..."
                )
            else:
                raise NotUniqueError(
                    f"Data point {x} is not unique. You can set"
                    ' "allow_duplicate_points=True" to avoid this error'
                )

        # if x is not within the bounds of the parameter space, warn the user
        if self._bounds is not None:
            if not np.all((self._bounds[:, 0] <= x) & (x <= self._bounds[:, 1])):
                warn(
                    f"\nData point {x} is outside the bounds of the "
                    + "parameter space. ",
                    stacklevel=2,
                )

        self._params = np.concatenate([self._params, x.reshape(1, -1)]).astype(
            self.dtype
        )
        self._target = np.concatenate([self._target, [target]])

        if self._constraint is None:
            # Insert data into unique dictionary
            self._cache[_hashable(x.ravel())] = target
        else:
            if constraint_value is None:
                msg = (
                    "When registering a point to a constrained TargetSpace"
                    + " a constraint value needs to be present."
                )
                raise ValueError(msg)
            # Insert data into unique dictionary
            self._cache[_hashable(x.ravel())] = (target, constraint_value)
            self._constraint_values = np.concatenate(
                [self._constraint_values, [constraint_value]]
            )

    def max(self):
        """Get maximum target value found and corresponding parameters.

        If there is a constraint present, the maximum value that fulfills the
        constraint within the parameter bounds is returned.

        Returns
        -------
        res: dict
            A dictionary with the keys 'target' and 'params'. The value of
            'target' is the maximum target value, and the value of 'params' is
            a dictionary with the parameter names as keys and the parameter
            values as values.
        """
        target_max = self._target_max()
        if target_max is None:
            return None

        target = self.target[self.mask]
        params = self.params[self.mask]
        target_max_idx = np.argmax(target)

        res = {
            "target": target_max,
            "params": dict(zip(self.keys, params[target_max_idx])),
        }

        if self._constraint is not None:
            constraint_values = self.constraint_values[self.mask]
            res["constraint"] = constraint_values[target_max_idx]

        return res

    def min(self):
        """Get minimum target value found and corresponding parameters.

        If there is a constraint present, the minimum value that fulfills the
        constraint within the parameter bounds is returned.

        Returns
        -------
        res: dict
            A dictionary with the keys 'target' and 'params'. The value of
            'target' is the minimum target value, and the value of 'params' is
            a dictionary with the parameter names as keys and the parameter
            values as values.
        """
        target_min = self._target_min()
        if target_min is None:
            return None

        target = self.target[self.mask]
        params = self.params[self.mask]
        target_min_idx = np.argmin(target)

        res = {
            "target": target_min,
            "params": dict(zip(self.keys, params[target_min_idx])),
        }

        if self._constraint is not None:
            constraint_values = self.constraint_values[self.mask]
            res["constraint"] = constraint_values[target_min_idx]

        return res

    def _as_array(self, x):
        try:
            x = np.asarray(x, dtype=self.dtype)
        except TypeError:
            x = self.params_to_array(x)

        x = x.ravel()
        if not x.size == self.dim:
            raise ValueError(
                f"Size of array ({len(x)}) is different than the "
                + f"expected number of parameters ({len(self.keys)})."
            )
        return x

    def _target_max(self):
        """Get the maximum target value within the current parameter bounds.

        If there is a constraint present, the maximum value that fulfills the
        constraint within the parameter bounds is returned.

        Returns
        -------
        max: float
            The maximum target value.
        """
        if len(self.target) == 0:
            return None

        if len(self.target[self.mask]) == 0:
            return None

        return self.target[self.mask].max()

    def _target_min(self):
        """Get the minimum target value within the current parameter bounds.

        If there is a constraint present, the minimum value that fulfills the
        constraint within the parameter bounds is returned.

        Returns
        -------
        min: float
            The minimum target value.
        """
        if len(self.target) == 0:
            return None

        if len(self.target[self.mask]) == 0:
            return None

        return self.target[self.mask].min()

    def clear_data(self):
        """Clear all data from this TargetSpace."""
        self._params = np.empty(shape=(0, self.dim))
        self._target = np.empty(shape=(0,))

        if self._constraint is not None:
            self._constraint_values = np.empty(shape=(0, self._constraint.lb.size))

        self._cache = {}

    def probe(self, params):
        """Evaluate the target function on a point and register the result.

        Notes
        -----
        If `params` has been previously seen and duplicate points are not
        allowed, returns a cached value of `result`.

        Parameters
        ----------
        params : np.ndarray
            a single point, with len(x) == self.dim

        Returns
        -------
        float | Tuple(float, float) : target function value,
            or Tuple(target function value, constraint value)

        Example
        -------
        >>> target_func = lambda p1, p2: p1 + p2
        >>> pbounds = {'p1': (0, 1), 'p2': (1, 100)}
        >>> space = TargetSpace(target_func, pbounds)
        >>> space.probe([1, 5])
        >>> assert self.max()['target'] == 6
        >>> assert self.max()['params'] == {'p1': 1.0, 'p2': 5.0}
        """
        x = self._as_array(params)
        if x in self:
            if not self._allow_duplicate_points:
                return self._cache[_hashable(x.ravel())]

        params = dict(zip(self._keys, x))
        target = self.target_func(**params)

        if self._constraint is None:
            self.register(x, target)
            return target

        constraint_value = self._constraint.eval(**params)
        self.register(x, target, constraint_value)
        return target, constraint_value

    def res(self):
        """Get all target values and constraint fulfillment for all parameters.

        Returns
        -------
        res: list
            A list of dictionaries with the keys 'target', 'params', and
            'constraint'. The value of 'target' is the target value, the value
            of 'params' is a dictionary with the parameter names as keys and
            the parameter values as values, and the value of 'constraint' is
            the constraint fulfillment.

        Notes
        -----
        Does not report if points are within the bounds of the parameter space.
        """
        if self._constraint is None:
            params = [dict(zip(self.keys, p)) for p in self.params]

            return [
                {
                    "target": target,
                    "params": param,
                    "hypotheses": names,
                }
                for target, param, names in zip(
                    self.target,
                    params,
                    self._hypothesis_tracking,
                )
            ]

        params = [dict(zip(self.keys, p)) for p in self.params]

        return [
            {
                "target": target,
                "constraint": constraint_value,
                "params": param,
                "allowed": allowed,
                "hypotheses": names,
            }
            for target, constraint_value, param, allowed, names in zip(
                self.target,
                self._constraint_values,
                params,
                self._constraint.allowed(self._constraint_values),
                self._hypothesis_tracking,
            )
        ]

    def get_data_in_tensors(self):
        """Get the data in tensors."""
        X = torch.tensor(self.params)
        Y = torch.tensor(self.target).view(-1, 1)
        return X, Y

    def set_bounds(self, new_bounds):
        """Change the lower and upper search bounds.

        Parameters
        ----------
        new_bounds : dict
            A dictionary with the parameter name and its new bounds
        """
        for row, key in enumerate(self.keys):
            if key in new_bounds:
                self._bounds[row] = new_bounds[key]


class TargetSpace(Space):
    """Holds the param-space coordinates (X) and target values (Y).

    Allows for constant-time appends.

    Parameters
    ----------
    target_func : function
        Function to be maximized.

    pbounds : dict
        Dictionary with parameters names as keys and a tuple with minimum
        and maximum values.

    random_state : int, RandomState, or None
        optionally specify a seed for a random number generator

    allow_duplicate_points: bool, optional (default=False)
        If True, the optimizer will allow duplicate points to be registered.
        This behavior may be desired in high noise situations where repeatedly
        probing the same point will give different answers. In other
        situations, the acquisition may occasionally generate a duplicate
        point.

    Examples
    --------
    >>> def target_func(p1, p2):
    >>>     return p1 + p2
    >>> pbounds = {'p1': (0, 1), 'p2': (1, 100)}
    >>> space = TargetSpace(target_func, pbounds, random_state=0)
    >>> x = np.array([4 , 5])
    >>> y = target_func(x)
    >>> space.register(x, y)
    >>> assert self.max()['target'] == 9
    >>> assert self.max()['params'] == {'p1': 1.0, 'p2': 2.0}
    """

    def __init__(
        self,
        target_func,
        pbounds,
        key_order: List[str] = None,
        constraint=None,
        random_state=None,
        allow_duplicate_points=False,
        discretization_steps=None,
    ):

        self.target_func = target_func  # The function to be optimized
        self._discretization_steps = discretization_steps
        super(TargetSpace, self).__init__(
            pbounds=pbounds,
            key_order=key_order,
            constraint=constraint,
            random_state=random_state,
            allow_duplicate_points=allow_duplicate_points,
        )

    def _generate_points_with_constraint(
        self,
        n: int,
        cache: Dict[str, None],
    ) -> np.ndarray:
        """Generate random samples that fulfill the constraint.

        Parameters
        ----------
        n : int
            Number of samples to generate.
        cache : Dict[str, None]
            A dictionary to store the generated samples.

        Returns
        -------
        np.ndarray: Random samples that fulfill the constraint.
        """
        n_cache_init = len(cache)
        samples = self._constraint.generate_random_points_fct(n=n, bounds=self._bounds)
        add_samples_to_cache(samples, cache)
        if len(cache) - n_cache_init < n:
            for i in range(100):
                remainder = n - (len(cache) - n_cache_init)
                xs = self._constraint.generate_random_points_fct(
                    n=remainder, bounds=self._bounds
                )
                for x in xs:
                    if _hashable(x.ravel()) not in cache:
                        samples = np.append(samples, [x], axis=0)
                        cache[_hashable(x.ravel())] = None
                if len(samples) == n:
                    break
        return samples

    def _generate_points_without_constraint(
        self,
        n: int,
        cache: Dict[str, None],
    ):
        """
        Generate samples within the specified bounds without any constraints.

        Parameters:
        ----------
        n : int
            Number of samples to generate.

        cache : dict, optional
            A dictionary to cache generated samples to avoid duplicates.

        Returns:
        -------
            np.ndarray: An array of generated samples.
        """
        samples = []
        while len(samples) < n:
            # Generate a random sample within the bounds
            sample = self._random_state.uniform(
                self._bounds[:, 0], self._bounds[:, 1], size=self._bounds.shape[0]
            )
            # Discretize the sample if discretization steps are defined
            if self._discretization_steps is not None:
                sample = self.discretize_point(sample)
            # Check if the sample is already in the cache
            if _hashable(sample.ravel()) not in cache:
                samples.append(sample)
                cache[_hashable(sample.ravel())] = None
        return np.array(samples)

    def random_points(self, n: int, cache: Dict = {}) -> np.ndarray:
        """
        Generate random points within the bounds of the parameter space.

        Parameters
        ----------
        n : int
            Number of points to generate.

        cache : dict, optional
            A dictionary to store the generated points.

        Returns
        -------
        np.ndarray
            An array of generated points
        """

        # If cache is empty, use the cache of the Space
        if len(cache) == 0:
            cache = deepcopy(self._cache)
        else:
            # Merge the cache with the cache of the Space
            cache.update(self._cache)

        points = []
        # If there is a constraint, generate points that fulfill the
        # constraint
        if self._constraint:
            if self._constraint.generate_random_points_fct:
                points = self._generate_points_with_constraint(n, cache)
            else:
                while len(points) < n:
                    # Generate points randomly
                    xs = self._random_state.uniform(
                        self._bounds[:, 0],
                        self._bounds[:, 1],
                        size=(n - len(points), self._bounds.shape[0]),
                    )

                    # Add the points that fulfill the constraint
                    for x in xs:
                        if self._discretization_steps is not None:
                            x = self.discretize_point(x)
                        value = self._constraint.eval(**dict(zip(self._keys, x)))
                        if self._constraint.allowed(value):
                            if _hashable(x.ravel()) not in cache:
                                points.append(x)
                                cache[_hashable(x.ravel())] = None
                        if len(points) == n:
                            break

        # If there is no constraint, generate points without constraint
        else:
            points = self._generate_points_without_constraint(n, cache)

        if len(points) == 0:
            raise ValueError("Failed to generate a random point.")
        return points

    def discretize_point(self, point: np.ndarray) -> np.ndarray:
        """
        Discretize a point according to the discretization steps.

        Parameters:
        ----------
            point (np.ndarray): A point to discretize.

        Returns:
            np.ndarray: The discretized point.
        """
        discretized_point = []
        for i, value in enumerate(point):
            lower, upper = self._bounds[i]
            step = self._discretization_steps[i]
            # Ensure the value is within bounds
            value = max(lower, min(value, upper))
            # Discretize the value
            discretized_value = math.floor((value - lower) / step) * step + lower
            discretized_point.append(discretized_value)
        return np.array(discretized_point)
