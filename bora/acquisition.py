"""Acquisition functions for Bayesian Optimization."""

from __future__ import annotations

import abc
import warnings
from copy import deepcopy
from numbers import Number
from typing import TYPE_CHECKING, Callable

import numpy as np
from numpy.random import RandomState
from scipy.optimize import minimize
from scipy.special import softmax
from scipy.stats import norm
from sklearn.gaussian_process import GaussianProcessRegressor

from bora.target_space import TargetSpace
from bora.util import (ConstraintNotSupportedError,
                       NoValidPointRegisteredError, TargetSpaceEmptyError)

if TYPE_CHECKING:
    from bora.constraint import ConstraintModel


class AcquisitionFunction(abc.ABC):
    """Base class for acquisition functions.

    Parameters
    ----------
    random_state : int, RandomState, default None
        Set the random state for reproducibility.
    """

    def __init__(self, random_state=None):
        if random_state is not None:
            if isinstance(random_state, RandomState):
                self.random_state = random_state
            else:
                self.random_state = RandomState(random_state)
        else:
            self.random_state = RandomState()
        self.i = 0

    @abc.abstractmethod
    def base_acq(self, *args, **kwargs):
        """Provide access to the base acquisition function."""

    def _fit_gp(self, gp: GaussianProcessRegressor,
                target_space: TargetSpace) -> None:
        # Sklearn's GP throws a large number of warnings at times, but
        # we don't really need to see them here.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            gp.fit(target_space.params, target_space.target)
            if target_space.constraint is not None:
                target_space.constraint.fit(target_space.params,
                                            target_space._constraint_values)

    def suggest(
        self,
        gp: GaussianProcessRegressor,
        target_space: TargetSpace,
        n_random=10_000,
        n_l_bfgs_b=20,
        fit_gp: bool = True,
        n: int = 1,
    ):
        """Suggest a promising point to probe next.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        target_space : TargetSpace
            The target space to probe.

        n_random : int, default 10_000
            Number of random samples to use.

        n_l_bfgs_b : int, default 10
            Number of starting points for the L-BFGS-B optimizer.

        fit_gp : bool, default True
            Whether to fit the Gaussian Process to the target space.
            Set to False if the GP is already fitted.

        Returns
        -------
        np.ndarray
            Suggested point to probe next.
        """
        if len(target_space) == 0:
            msg = ("Cannot suggest a point without previous samples. Use "
                   " target_space.random_sample() to generate a point and "
                   " target_space.probe(*) to evaluate it.")
            raise TargetSpaceEmptyError(msg)
        self.i += 1
        if fit_gp:
            self._fit_gp(gp=gp, target_space=target_space)

        acq = self._get_acq(gp=gp, constraint=target_space.constraint)
        suggestions = self._acq_min(
            acq,
            target_space,
            n_random=n_random,
            n_l_bfgs_b=n_l_bfgs_b,
            n=n,
        )
        return suggestions

    def _get_acq(self,
                 gp: GaussianProcessRegressor,
                 constraint: ConstraintModel | None = None) -> Callable:
        """Prepare the acquisition function for minimization.

        Transforms a base_acq Callable, which takes `mean` and `std` as
        input, into an acquisition function that only requires an array of
        parameters.
        Handles GP predictions and constraints.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        constraint : ConstraintModel, default None
            A fitted constraint model, if constraints are present and the
            acquisition function supports them.

        Returns
        -------
        Callable
            Function to minimize.
        """
        dim = gp.X_train_.shape[1]
        if constraint is not None:

            def acq(x):
                x = x.reshape(-1, dim)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    mean, std = gp.predict(x, return_std=True)
                    p_constraints = constraint.predict(x)
                return -1 * self.base_acq(mean, std) * p_constraints
        else:

            def acq(x):
                x = x.reshape(-1, dim)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    mean, std = gp.predict(x, return_std=True)
                return -1 * self.base_acq(mean, std)

        return acq

    def _acq_min(
        self,
        acq: Callable,
        target_space: TargetSpace,
        n_random=10_000,
        n_l_bfgs_b=10,
        n: int = 1,
    ) -> np.ndarray:
        """Find the maximum of the acquisition function.

        Uses a combination of random sampling (cheap) and the 'L-BFGS-B'
        optimization method. First by sampling `n_warmup` (1e5) points at
        random,
        and then running L-BFGS-B from `n_iter` (10) random starting points.

        Parameters
        ----------
        acq : Callable
            Acquisition function to use. Should accept an array of parameters
            `x`.

        bounds : np.ndarray
            Bounds of the search space. For `N` parameters this has shape
            `(N, 2)` with `[i, 0]` the lower bound of parameter `i` and
            `[i, 1]` the upper bound.

        n_random : int
            Number of random samples to use.

        n_l_bfgs_b : int
            Number of starting points for the L-BFGS-B optimizer.

        Returns
        -------
        np.ndarray
            Parameters maximizing the acquisition function.

        """
        if n_random == 0 and n_l_bfgs_b == 0:
            error_msg = "Either n_random or n_l_bfgs_b needs to be greater than 0."
            raise ValueError(error_msg)
        x_min_r, min_acq_r = self._random_sample_minimize(
            acq, target_space=target_space, n_random=n_random, n=n)

        x_min_l, min_acq_l = self._l_bfgs_b_minimize(acq,
                                                     target_space,
                                                     n_x_seeds=n_l_bfgs_b,
                                                     n=n)
        # Merge random search and L-BFGS-B results
        if len(x_min_r) == 0:
            return x_min_l
        elif len(x_min_l) == 0:
            return x_min_r

        x_mins = np.concatenate([x_min_r, x_min_l], axis=0)
        min_acqs = np.concatenate([min_acq_r, min_acq_l], axis=0)

        # Get the best n results
        indx = np.argsort(min_acqs)[:n]
        x_mins = x_mins[indx]
        return x_mins

    def _random_sample_minimize(
        self,
        acq: Callable,
        target_space: TargetSpace,
        n_random: int,
        n: int = 1,
    ) -> tuple[np.ndarray, float]:
        """Random search to find the minimum of `acq` function.

        Parameters
        ----------
        acq : Callable
            Acquisition function to use. Should accept an array of parameters
            `x`.

        n_random : int
            Number of random samples to use.

        Returns
        -------
        x_min : np.ndarray
            Random sample minimizing the acquisition function.

        min_acq : float
            Acquisition function value at `x_min`
        """
        if n_random == 0:
            return None, np.inf

        x_tries = target_space.random_points(n_random)

        # If no random sample satisfies the constraints, return None
        if len(x_tries) == 0:
            return None, np.inf

        # Evaluate the acquisition function at all random samples
        ys = acq(x_tries)

        # Keep the n best samples with the lowest acquisition function value
        indx = np.argsort(ys)[:n]
        x_min = x_tries[indx]
        min_acq = ys[indx]
        return x_min, min_acq

    def _l_bfgs_b_minimize(self,
                           acq: Callable,
                           target_space: TargetSpace,
                           n_x_seeds: int = 10,
                           n: int = 1) -> tuple[list[np.ndarray], list[float]]:
        """Random search to find the minimum of `acq` function.

        Parameters
        ----------
        acq : Callable
            Acquisition function to use. Should accept an array of parameters
            `x`.

        n_x_seeds : int
            Number of starting points for the L-BFGS-B optimizer.

        n : int
            Number of best results to return.

        Returns
        -------
        x_mins : list[np.ndarray]
            List of minimal results of the L-BFGS-B optimizer.

        min_acqs : list[float]
            List of acquisition function values at `x_mins`
        """
        if n_x_seeds == 0:
            return [], []

        # Generate starting points for the L-BFGS-B optimizer
        x_seeds = target_space.random_points(n_x_seeds)

        results = []
        for x_try in x_seeds:
            # Find the minimum of minus the acquisition function
            res = minimize(acq,
                           x_try,
                           bounds=target_space.bounds,
                           method="L-BFGS-B")

            # Clip output to make sure it lies within the bounds. Due to floating
            # point technicalities this is not always the case.
            x_min = np.clip(res.x, target_space.bounds[:, 0],
                            target_space.bounds[:, 1])

            if target_space._discretization_steps is not None:
                x_min = target_space.discretize_point(x_min)

            # See if success
            if not res.success:
                continue
            else:
                if target_space.constraint is not None:
                    value = target_space.constraint.eval(
                        **dict(zip(target_space.keys, x_min)))
                    allowed = target_space.constraint.allowed(value)
                    if np.any(~allowed):
                        continue

            # Store the result
            results.append((x_min, np.squeeze(res.fun)))

        # Remove the results for which x_min is in target_space
        if not target_space._allow_duplicate_points:
            results = [(x_min, min_acq) for x_min, min_acq in results
                       if x_min not in target_space]

        # Sort results by acquisition function value
        results.sort(key=lambda x: x[1])

        # Get the best n results
        best_results = results[:n]

        # Separate x_mins and min_acqs
        x_mins, min_acqs = zip(*best_results) if best_results else ([], [])

        return list(x_mins), list(min_acqs)


class UpperConfidenceBound(AcquisitionFunction):
    r"""Upper Confidence Bound acquisition function.

    The upper confidence bound is calculated as

    .. math::
        \text{UCB}(x) = \mu(x) + \kappa \sigma(x).

    Parameters
    ----------
    kappa : float, default 2.576
        Governs the exploration/exploitation tradeoff. Lower prefers
        exploitation, higher prefers exploration.

    exploration_decay : float, default None
        Decay rate for kappa. If None, no decay is applied.

    exploration_decay_delay : int, default None
        Delay for decay. If None, decay is applied from the start.

    random_state : int, RandomState, default None
        Set the random state for reproducibility.

    """

    def __init__(self,
                 kappa=2.576,
                 exploration_decay=None,
                 exploration_decay_delay=None,
                 random_state=None) -> None:
        if kappa < 0:
            error_msg = "kappa must be greater than or equal to 0."
            raise ValueError(error_msg)

        super().__init__(random_state=random_state)
        self.kappa = kappa
        self.exploration_decay = exploration_decay
        self.exploration_decay_delay = exploration_decay_delay

    def base_acq(self, mean, std):
        """Calculate the upper confidence bound.

        Parameters
        ----------
        mean : np.ndarray
            Mean of the predictive distribution.

        std : np.ndarray
            Standard deviation of the predictive distribution.

        Returns
        -------
        np.ndarray
            Acquisition function value.
        """
        return mean + self.kappa * std

    def suggest(
        self,
        gp: GaussianProcessRegressor,
        target_space: TargetSpace,
        n_random: int = 10_000,
        n_l_bfgs_b: int = 10,
        fit_gp: bool = True,
    ) -> np.ndarray:
        """Suggest a promising point to probe next.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        target_space : TargetSpace
            The target space to probe.

        n_random : int, default 10_000
            Number of random samples to use.

        n_l_bfgs_b : int, default 10
            Number of starting points for the L-BFGS-B optimizer.

        fit_gp : bool, default True
            Whether to fit the Gaussian Process to the target space.
            Set to False if the GP is already fitted.

        Returns
        -------
        np.ndarray
            Suggested point to probe next.
        """
        if target_space.constraint is not None:
            msg = (
                f"Received constraints, but acquisition function {type(self)} "
                "does not support constrained optimization.")
            raise ConstraintNotSupportedError(msg)
        x_max = super().suggest(gp=gp,
                                target_space=target_space,
                                n_random=n_random,
                                n_l_bfgs_b=n_l_bfgs_b,
                                fit_gp=fit_gp)
        self.decay_exploration()
        return x_max

    def decay_exploration(self) -> None:
        """Decay kappa by a constant rate.

        Adjust exploration/exploitation trade-off by reducing kappa.
        """
        if self.exploration_decay is not None and (
                self.exploration_decay_delay is None
                or self.exploration_decay_delay <= self.i):
            self.kappa = self.kappa * self.exploration_decay


class ProbabilityOfImprovement(AcquisitionFunction):
    r"""Probability of Improvement acqusition function.

    Calculated as

    .. math:: \text{POI}(x) = \Phi\left( \frac{\mu(x)-y_{\text{max}} -
    \xi }{\sigma(x)} \right)

    where :math:`\Phi` is the CDF of the normal distribution.

    Parameters
    ----------
    xi : float, positive
        Governs the exploration/exploitation tradeoff. Lower prefers
        exploitation, higher prefers exploration.

    exploration_decay : float, default None
        Decay rate for xi. If None, no decay is applied.

    exploration_decay_delay : int, default None
        Delay for decay. If None, decay is applied from the start.

    random_state : int, RandomState, default None
        Set the random state for reproducibility.
    """

    def __init__(self,
                 xi,
                 exploration_decay=None,
                 exploration_decay_delay=None,
                 random_state=None) -> None:
        super().__init__(random_state=random_state)
        self.xi = xi
        self.exploration_decay = exploration_decay
        self.exploration_decay_delay = exploration_decay_delay
        self.y_max = None

    def base_acq(self, mean, std):
        """Calculate the probability of improvement.

        Parameters
        ----------
        mean : np.ndarray
            Mean of the predictive distribution.

        std : np.ndarray
            Standard deviation of the predictive distribution.

        Returns
        -------
        np.ndarray
            Acquisition function value.

        Raises
        ------
        ValueError
            If y_max is not set.
        """
        if self.y_max is None:
            msg = ("y_max is not set. If you are calling this method outside "
                   "of suggest(), you must set y_max manually.")
            raise ValueError(msg)
        z = (mean - self.y_max - self.xi) / std
        return norm.cdf(z)

    def suggest(
        self,
        gp: GaussianProcessRegressor,
        target_space: TargetSpace,
        n_random=10_000,
        n_l_bfgs_b=10,
        fit_gp: bool = True,
    ) -> np.ndarray:
        """Suggest a promising point to probe next.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        target_space : TargetSpace
            The target space to probe.

        n_random : int, default 10_000
            Number of random samples to use.

        n_l_bfgs_b : int, default 10
            Number of starting points for the L-BFGS-B optimizer.

        fit_gp : bool, default True
            Whether to fit the Gaussian Process to the target space.
            Set to False if the GP is already fitted.

        Returns
        -------
        np.ndarray
            Suggested point to probe next.
        """
        y_max = target_space._target_max()
        if y_max is None and not target_space.empty:
            # If target space is empty, let base class handle the error
            msg = (
                "Cannot suggest a point without an allowed point. Use "
                "target_space.random_sample() to generate a point until "
                " at least one point that satisfies the constraints is found.")
            raise NoValidPointRegisteredError(msg)
        self.y_max = y_max
        x_max = super().suggest(gp=gp,
                                target_space=target_space,
                                n_random=n_random,
                                n_l_bfgs_b=n_l_bfgs_b,
                                fit_gp=fit_gp)
        self.decay_exploration()
        return x_max

    def decay_exploration(self) -> None:
        r"""Decay xi by a constant rate.

        Adjust exploration/exploitation trade-off by reducing xi.
        """
        if self.exploration_decay is not None and (
                self.exploration_decay_delay is None
                or self.exploration_decay_delay <= self.i):
            self.xi = self.xi * self.exploration_decay


class ExpectedImprovement(AcquisitionFunction):
    r"""Expected Improvement acqusition function.

    Similar to Probability of Improvement (`ProbabilityOfImprovement`), but
    also considers the magnitude of improvement.
    Calculated as

    .. math::
        \text{EI}(x) = (\mu(x)-y_{\text{max}} - \xi) \Phi\left(
            \frac{\mu(x)-y_{\text{max}} -  \xi }{\sigma(x)} \right)
                + \sigma(x) \phi\left(
                \frac{\mu(x)-y_{\text{max}} -  \xi }{\sigma(x)} \right)

    where :math:`\Phi` is the CDF and :math:`\phi` the PDF of the normal
    distribution.

    Parameters
    ----------
    xi : float, positive
        Governs the exploration/exploitation tradeoff. Lower prefers
        exploitation, higher prefers exploration.

    exploration_decay : float, default None
        Decay rate for xi. If None, no decay is applied.

    exploration_decay_delay : int, default None

    random_state : int, RandomState, default None
        Set the random state for reproducibility.
    """

    def __init__(self,
                 xi,
                 exploration_decay=None,
                 exploration_decay_delay=None,
                 random_state=None) -> None:
        super().__init__(random_state=random_state)
        self.xi = xi
        self.exploration_decay = exploration_decay
        self.exploration_decay_delay = exploration_decay_delay
        self.y_max = None

    def base_acq(self, mean, std):
        """Calculate the expected improvement.

        Parameters
        ----------
        mean : np.ndarray
            Mean of the predictive distribution.

        std : np.ndarray
            Standard deviation of the predictive distribution.

        Returns
        -------
        np.ndarray
            Acquisition function value.

        Raises
        ------
        ValueError
            If y_max is not set.
        """
        if self.y_max is None:
            msg = ("y_max is not set. If you are calling this method outside "
                   "of suggest(), ensure y_max is set, or set it manually.")
            raise ValueError(msg)
        a = mean - self.y_max - self.xi
        z = a / std
        return a * norm.cdf(z) + std * norm.pdf(z)

    def suggest(
        self,
        gp: GaussianProcessRegressor,
        target_space: TargetSpace,
        # y_max: float,
        n_random=10_000,
        n_l_bfgs_b=10,
        fit_gp: bool = True,
        n: int = 1,
    ) -> np.ndarray:
        """Suggest a promising point to probe next.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        target_space : TargetSpace
            The target space to probe.

        n_random : int, default 10_000
            Number of random samples to use.

        n_l_bfgs_b : int, default 10
            Number of starting points for the L-BFGS-B optimizer.

        fit_gp : bool, default True
            Whether to fit the Gaussian Process to the target space.
            Set to False if the GP is already fitted.

        Returns
        -------
        np.ndarray
            Suggested point to probe next.
        """
        y_max = target_space._target_max()
        if y_max is None and not target_space.empty:
            # If target space is empty, let base class handle the error
            msg = (
                "Cannot suggest a point without an allowed point. Use "
                "target_space.random_sample() to generate a point until "
                " at least one point that satisfies the constraints is found.")
            raise NoValidPointRegisteredError(msg)
        self.y_max = y_max

        x_maxs = super().suggest(
            gp=gp,
            target_space=target_space,
            n_random=n_random,
            n_l_bfgs_b=n_l_bfgs_b,
            fit_gp=fit_gp,
            n=n,
        )
        if target_space.constraint is not None:
            for i in range(len(x_maxs)):
                x = x_maxs[i]
                value = target_space.constraint.eval(
                    **target_space.array_to_params(x))
                allowed = target_space.constraint.allowed(value)
                if np.all(allowed):
                    self.decay_exploration()
                else:
                    x = target_space.random_points(n=1)[0]
                    x_maxs[i] = x
        else:
            self.decay_exploration()
        return x_maxs

    def decay_exploration(self) -> None:
        r"""Decay xi by a constant rate.

        Adjust exploration/exploitation trade-off by reducing xi.
        """
        if self.exploration_decay is not None and (
                self.exploration_decay_delay is None
                or self.exploration_decay_delay <= self.i):
            self.xi = self.xi * self.exploration_decay


class ConstantLiar(AcquisitionFunction):
    """Constant Liar acquisition function.

    Used for asynchronous optimization. It operates on a copy of the target
    space that includes the previously suggested points that have not been
    evaluated yet. A GP fitted to this target space is less likely to suggest
    the same point again, since the variance of the predictive distribution
    is lower at these points. This is discourages the optimization algorithm
    from suggesting the same point to multiple workers.

    Parameters
    ----------
    base_acquisition : AcquisitionFunction
        The acquisition function to use.

    strategy : float or str, default 'max'
        Strategy to use for the constant liar. If a float, the constant liar
        will always register dummies with this value. If 'min'/'mean'/'max',
        the constant liar will register dummies with the minimum/mean/maximum
        target value in the target space.

    random_state : int, RandomState, default None
        Set the random state for reproducibility.

    atol : float, default 1e-5
        Absolute tolerance to eliminate a dummy point.

    rtol : float, default 1e-8
        Relative tolerance to eliminate a dummy point.
    """

    def __init__(self,
                 base_acquisition: AcquisitionFunction,
                 strategy="max",
                 random_state=None,
                 atol=1e-5,
                 rtol=1e-8) -> None:
        super().__init__(random_state)
        self.base_acquisition = base_acquisition
        self.dummies = []
        if not isinstance(strategy, Number) and strategy not in [
                "min", "mean", "max"
        ]:
            error_msg = f"Received invalid argument {strategy} for strategy."
            raise ValueError(error_msg)
        self.strategy = strategy
        self.atol = atol
        self.rtol = rtol

    def base_acq(self, *args, **kwargs):
        """Calculate the acquisition function.

        Calls the base acquisition function's `base_acq` method.

        Returns
        -------
        np.ndarray
            Acquisition function value.
        """
        return self.base_acquisition.base_acq(*args, **kwargs)

    def _copy_target_space(self, target_space: TargetSpace) -> TargetSpace:
        """Create a copy of the target space.

        Parameters
        ----------
        target_space : TargetSpace
            The target space to copy.

        Returns
        -------
        TargetSpace
            A copy of the target space.
        """
        keys = target_space.keys
        pbounds = {key: bound for key, bound in zip(keys, target_space.bounds)}
        target_space_copy = TargetSpace(
            None,
            pbounds=pbounds,
            constraint=target_space.constraint,
            allow_duplicate_points=target_space._allow_duplicate_points,
        )
        target_space_copy._params = deepcopy(target_space._params)
        target_space_copy._target = deepcopy(target_space._target)

        return target_space_copy

    def _remove_expired_dummies(self, target_space: TargetSpace) -> None:
        """Remove expired dummy points from the list of dummies.

        Once a worker has evaluated a dummy point, the dummy is discarded. To
        accomplish this, we compare every dummy point to the current target
        space's parameters and remove it if it is close to any of them.

        Parameters
        ----------
        target_space : TargetSpace
            The target space to compare the dummies to.
        """
        dummies = []
        for dummy in self.dummies:
            close = np.isclose(dummy,
                               target_space.params,
                               rtol=self.rtol,
                               atol=self.atol)
            if not close.all(axis=1).any():
                dummies.append(dummy)
        self.dummies = dummies

    def suggest(
        self,
        gp: GaussianProcessRegressor,
        target_space: TargetSpace,
        n_random=10_000,
        n_l_bfgs_b=10,
        fit_gp: bool = True,
    ) -> np.ndarray:
        """Suggest a promising point to probe next.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        target_space : TargetSpace
            The target space to probe.

        n_random : int, default 10_000
            Number of random samples to use.

        n_l_bfgs_b : int, default 10
            Number of starting points for the L-BFGS-B optimizer.

        fit_gp : bool, default True
            Whether to fit the Gaussian Process to the target space.
            Set to False if the GP is already fitted.

        Returns
        -------
        np.ndarray
            Suggested point to probe next.
        """
        if len(target_space) == 0:
            msg = ("Cannot suggest a point without previous samples. Use "
                   " target_space.random_sample() to generate a point and "
                   " target_space.probe(*) to evaluate it.")
            raise TargetSpaceEmptyError(msg)

        if target_space.constraint is not None:
            msg = (
                f"Received constraints, but acquisition function {type(self)} "
                "does not support constrained optimization.")
            raise ConstraintNotSupportedError(msg)

        # Check if any dummies have been evaluated and remove them
        self._remove_expired_dummies(target_space)

        # Create a copy of the target space
        dummy_target_space = self._copy_target_space(target_space)

        # Choose the dummy target value
        if isinstance(self.strategy, Number):
            dummy_target = self.strategy
        elif self.strategy == "min":
            dummy_target = target_space.target.min()
        elif self.strategy == "mean":
            dummy_target = target_space.target.mean()
        elif self.strategy != "max":
            error_msg = f"Received invalid argument {self.strategy} for strategy."
            raise ValueError(error_msg)
        else:
            dummy_target = target_space.target.max()

        # Register the dummies to the dummy target space
        for dummy in self.dummies:
            dummy_target_space.register(dummy, dummy_target)

        # Fit the GP to the dummy target space and suggest a point
        self._fit_gp(gp=gp, target_space=dummy_target_space)
        x_max = self.base_acquisition.suggest(gp,
                                              dummy_target_space,
                                              n_random=n_random,
                                              n_l_bfgs_b=n_l_bfgs_b,
                                              fit_gp=False)

        # Register the suggested point as a dummy
        self.dummies.append(x_max)

        return x_max


class GPHedge(AcquisitionFunction):
    """GPHedge acquisition function.

    At each suggestion step, GPHedge samples suggestions from each base
    acquisition function acq_i. Then a candidate is selected from the
    suggestions based on the on the cumulative rewards of each acq_i.
    After evaluating the candidate, the gains are updated (in the next
    iteration) based on the updated expectation value of the candidates.

    For more information, see:
        Brochu et al., "Portfolio Allocation for Bayesian Optimization",
        https://arxiv.org/abs/1009.5419

    Parameters
    ----------
    base_acquisitions : List[AcquisitionFunction]
        List of base acquisition functions.

    random_state : int, RandomState, default None
        Set the random state for reproducibility.
    """

    def __init__(self,
                 base_acquisitions: list[AcquisitionFunction],
                 random_state=None) -> None:
        super().__init__(random_state)
        self.base_acquisitions = base_acquisitions
        self.n_acq = len(self.base_acquisitions)
        self.gains = np.zeros(self.n_acq)
        self.previous_candidates = None

    def base_acq(self, *args, **kwargs):
        """Raise an error, since the base acquisition function is ambiguous."""
        msg = (
            "GPHedge base acquisition function is ambiguous."
            " You may use self.base_acquisitions[i].base_acq(mean, std)"
            " to get the base acquisition function for the i-th acquisition.")
        raise TypeError(msg)

    def _sample_idx_from_softmax_gains(self) -> int:
        """Sample an index weighted by the softmax of the gains."""
        cumsum_softmax_g = np.cumsum(softmax(self.gains))
        r = self.random_state.rand()
        return np.argmax(r <= cumsum_softmax_g)  # Returns the first True value

    def _update_gains(self, gp: GaussianProcessRegressor) -> None:
        """Update the gains of the base acquisition functions."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            rewards = gp.predict(self.previous_candidates)
        self.gains += rewards
        self.previous_candidates = None

    def suggest(
        self,
        gp: GaussianProcessRegressor,
        target_space: TargetSpace,
        n_random=10_000,
        n_l_bfgs_b=10,
        fit_gp: bool = True,
    ) -> np.ndarray:
        """Suggest a promising point to probe next.

        Parameters
        ----------
        gp : GaussianProcessRegressor
            A fitted Gaussian Process.

        target_space : TargetSpace
            The target space to probe.

        n_random : int, default 10_000
            Number of random samples to use.

        n_l_bfgs_b : int, default 10
            Number of starting points for the L-BFGS-B optimizer.

        fit_gp : bool, default True
            Whether to fit the Gaussian Process to the target space.
            Set to False if the GP is already fitted.

        Returns
        -------
        np.ndarray
            Suggested point to probe next.
        """
        if len(target_space) == 0:
            msg = ("Cannot suggest a point without previous samples. Use "
                   " target_space.random_sample() to generate a point and "
                   " target_space.probe(*) to evaluate it.")
            raise TargetSpaceEmptyError(msg)
        self.i += 1
        if fit_gp:
            self._fit_gp(gp=gp, target_space=target_space)

        # Update the gains of the base acquisition functions
        if self.previous_candidates is not None:
            self._update_gains(gp)

        # Suggest a point using each base acquisition function
        x_max = [
            base_acq.suggest(
                gp=gp,
                target_space=target_space,
                n_random=n_random // self.n_acq,
                n_l_bfgs_b=n_l_bfgs_b // self.n_acq,
                fit_gp=False,
            ) for base_acq in self.base_acquisitions
        ]
        self.previous_candidates = np.array(x_max)
        idx = self._sample_idx_from_softmax_gains()
        return x_max[idx]
