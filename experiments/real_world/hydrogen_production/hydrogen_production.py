import json
import os
import pickle
import warnings

import numpy as np
import pandas as pd

from bora.constraint import ConstraintModel
from bora.experiment import Constraint, Experiment, Parameter, Target, Type
from bora.util import ensure_rng, hashable


class PhotocatalyticHydrogenProduction(Experiment):
    """Photocatalytic Hydrogen Production experiment."""

    def __init__(self, noisy: bool = False, random_seed: int = 0):
        # Load experiment from the experiment card
        current_dir = os.path.dirname(os.path.realpath(__file__))
        experiment_card_path = os.path.join(current_dir,
                                            "experiment_card.json")
        experiment_card = open(experiment_card_path)
        self._experiment_card = json.load(experiment_card)

        # Get the parameters
        parameters = []
        for parameter in self._experiment_card["parameters"]:
            name = parameter["name"]
            description = parameter["description"]
            bounds = parameter["bounds"]
            step = parameter["step"]
            p = Parameter(name=name,
                          type=Type.discrete,
                          description=description)
            p.set_bounds(bounds[0], bounds[1])
            p.set_step(step)
            parameters.append(p)

        target = Target(
            name=self._experiment_card["target"]["name"],
            description=self._experiment_card["target"]["description"],
        )
        self._load_gp(noisy)
        super().__init__(
            name=self._experiment_card["name"],
            description=self._experiment_card["description"],
            parameters=parameters,
            target=target,
            objective_function=self._get_objective_function(),
            constraint=self._get_constraint(random_seed),
            domain=self._experiment_card["domain"],
            default_precision=2,
            xopt=[0, 0.98, 0, 1.04, 0.75, 3.96, 0, 0, 0, 0.75],
            yopt=33.23,
        )

    def _load_gp(self, noisy: bool):
        """
        Load the GP model from the file.

        Parameters
        ----------
        noisy : bool
            If True, the GP model will be noisy.
        """
        current_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(current_dir, "her_model.pkl")
        with open(path, "rb") as file:
            # Sklearn's GP throws a large number of warnings at times, but
            # we don't really need to see them here.
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                gp = pickle.load(file)
                self.gp = gp
                self.noisy = noisy

    def _get_constraint(self, random_seed: int) -> Constraint:
        """
        Get the constraint for the experiment.

        Parameters
        ----------
        random_seed : int
            Random seed.

        Returns
        -------
        Constraint
            Constraint object.
        """

        def _cons(**kwargs):
            return sum(kwargs.values()) - kwargs["P10-MIX1"]

        cons = ConstraintModel(
            fun=_cons,
            lb=0,
            ub=5,
            random_state=random_seed,
            generate_random_points_fct=self.generate_random_points,
        )
        self._random_state = ensure_rng(random_seed)

        constraint = Constraint(
            description=self._experiment_card["constraint"],
            func=cons,
        )
        return constraint

    def _get_objective_function(self) -> callable:
        """
        Get the objective function for the experiment.

        Returns
        -------
        callable: Objective function.
        """

        def objective_function(x):
            x = np.atleast_2d(x)
            if self.noisy:
                x = x + np.random.uniform(-0.5, 0.5)
            x = pd.DataFrame(x, columns=self.keys)
            # Ignore the warning from the GP model
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                res = self.gp.predict(x)
                # If a value is negative set it to 0 as it is not possible
                res[res < 0] = 0
                return res

        return objective_function

    def generate_random_points(self,
                               n: int = 10,
                               bounds=None,
                               unit_scale=False) -> np.ndarray:
        """
        Generate random points in the feasible space.

        Parameters:
        ----------
            n (int, optional): Number of random points to generate.
            Defaults to 10.

        Returns:
        -------
            np.ndarray: Random points in the feasible space.
        """
        if bounds is None:
            point_lower_bounds = np.zeros(self.dim)
            point_lower_bounds[5] = 1
            point_upper_bounds = np.ones(self.dim) * 5
        else:
            point_lower_bounds, point_upper_bounds = zip(*bounds)
        sum_constraint = 5
        cache = {}

        points = []
        for i in range(n):
            sample = self._random_state.uniform(
                point_lower_bounds,
                point_upper_bounds,
            )
            sample_5 = sample[5]
            scale = sum_constraint / np.sum(sample)
            sample = sample * scale
            sample[5] = sample_5
            discretized_sample = self.discretize_sample(sample)
            _hash = hashable(discretized_sample)
            if _hash in cache:
                continue
            cache[_hash] = True
            points.append(discretized_sample)
        points = np.array(points)

        if unit_scale:
            points = (points - point_lower_bounds) / (point_upper_bounds -
                                                      point_lower_bounds)
        return points
