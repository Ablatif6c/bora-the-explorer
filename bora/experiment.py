import enum
from math import floor, isclose
from typing import Any, Callable, List

import numpy as np


class Type(enum.Enum):
    continuous = "continuous"
    discrete = "discrete"
    categorical = "categorical"


class CategoricalParameter:

    def __init__(self, name: str, categories: List[str]):
        self.name = name
        self.categories = categories

    def __repr__(self):
        return f"CategoricalParameter({self.name}, {self.categories})"


class Parameter:

    def __init__(
        self,
        name,
        type: Type,
        description: str,
    ):
        self.name = name
        self.type = type
        self.description = description

    def __repr__(self):
        return f"Parameter({self.name}"

    def set_categories(self, categories: List[str]):
        if self.type != Type.categorical:
            raise ValueError("Parameter is not categorical.")

        self.categories = categories

    def set_bounds(self, lb: float, ub: float):
        if self.type == Type.categorical:
            raise ValueError("Parameter is categorical.")
        self.lb = lb
        self.ub = ub

    def get_bounds(self):
        if self.type == Type.categorical:
            return 0, len(self.categories) - 1
        return self.lb, self.ub

    def set_step(self, step: float):
        if self.type != Type.discrete:
            raise ValueError("Parameter is not discrete.")
        self.step = step

    def is_valid_value(self, value):
        if self.type == Type.categorical:
            return value in self.categories
        if self.type == Type.discrete:
            for _length in range(0, int(self.ub / self.step) + 1):
                if isclose(_length * self.step, value):
                    return True
            return False
        return self.lb <= value <= self.ub


class Target:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Target({self.name}, {self.description}"


class Constraint:

    def __init__(
        self,
        description: str,
        func: Callable[[float], float],
    ):
        self.description = description
        self.constraint = func

    def __repr__(self):
        return f"Constraint({self.name}, {self.description}"


class Experiment:

    def __init__(
        self,
        name: str,
        description: str,
        parameters: List[Parameter],
        target: Target,
        objective_function: Callable[[float], float],
        domain: str,
        constraint: Constraint = None,
        default_precision: int = 3,
        xopt: List[float] = None,
        yopt: float = None,
    ):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.target = target
        self.objective_function = objective_function
        self.constraint = constraint
        self.domain = domain
        self.type = self.parameters[0].type
        self.default_precision = default_precision
        self.xopt = xopt
        self.yopt = yopt

    def __repr__(self):
        return (
            f"Experiment({self.name}, {self.description}, {self.parameters}"
            f", {self.target}, {self.domain})")

    @property
    def dim(self):
        return len(self.parameters)

    @property
    def keys(self):
        return [p.name for p in self.parameters]

    @property
    def pbounds(self):
        return {p.name: p.get_bounds() for p in self.parameters}

    @property
    def lb(self):
        return [p.lb for p in self.parameters]

    @property
    def ub(self):
        return [p.ub for p in self.parameters]

    @property
    def optimum(self):
        return (self.xopt, self.yopt)

    def get_parameter(self, name: str):
        for p in self.parameters:
            if p.name == name:
                return p
        return None

    def get_discretization_steps(self):
        if self.type != Type.discrete:
            return None
        steps = [p.step for p in self.parameters]
        return steps

    def discretize_sample(self, point):
        discretized_point = []
        for i, value in enumerate(point):
            lower, upper = self.parameters[i].get_bounds()
            step = self.parameters[i].step
            # Ensure the value is within bounds
            value = max(lower, min(value, upper))
            # Discretize the value
            discretized_value = floor((value - lower) / step) * step + lower
            discretized_point.append(discretized_value)
        return discretized_point

    def __call__(self, *args: Any, **kwargs: Any):
        # Evaluate the objective function based on the input data
        if args != ():
            res = self.objective_function(*args)
        else:
            # Ensure the keys in kwargs are ordered correctly
            ordered_values = [
                kwargs[key] for key in self.keys if key in kwargs
            ]

            input_data = np.array(ordered_values)
            res = self.objective_function(input_data)

        # Ensure the result is rounded to the default precision
        if len(res) == 1:
            res = round(res[0], self.default_precision)
        else:
            res = np.array([round(r, self.default_precision) for r in res])
        return res

    def generate_random_points(self, n: int, unit_scale=False):
        raise NotImplementedError

    def unit_scale(self, point):
        for i, value in enumerate(point):
            lower, upper = self.parameters[i].get_bounds()
            point[i] = (value - lower) / (upper - lower)


class CategoricalExperiment(Experiment):

    def __init__(
        self,
        name: str,
        description: str,
        parameters: List[Parameter],
        target: Target,
        objective_function: Callable[[float], float],
        domain: str,
        constraint: Constraint = None,
    ):
        super().__init__(name, description, parameters, target,
                         objective_function, domain, constraint)

    def get_n_vertices(self):
        vertices = []
        for p in self.parameters:
            if p.type == Type.categorical:
                v = len(p.categories)
                vertices.append(v)
            elif p.type == Type.discrete:
                v = int((p.ub - p.lb) / p.step) + 1
                vertices.append(v)
            else:
                # Continuous. Add 10 vertices.
                vertices.append(10)
        vertices = np.array(vertices)
        return vertices

    def map_categories_to_array(self, params):
        arr = [p.categories.index(params[p.name]) for p in self.parameters]
        return np.array(arr)

    def map_array_to_categories(self, arr):
        categories = [
            self.parameters[idx].categories[int(i)]
            for idx, i in enumerate(arr)
        ]
        return categories
