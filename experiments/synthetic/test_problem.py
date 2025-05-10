"""This script is a wrapper for the test problem class in the problem script.
It is used to create a test problem object that can be used in Bora.
The test problem object is created by passing the problem object to the
TestProblem class. The latter is a wrapper for the problem object that provides
the necessary attributes and methods to be used in Bora.
"""

from bora.experiment import Experiment, Parameter, Target, Type


class TestProblem(Experiment):
    """Wrapper for test problems to be used in Bora."""

    def __init__(self, problem, maximize=True):
        """
        Initialize the TestProblem object.

        Parameters
        ----------
        problem: The problem object.

        maximize: A boolean indicating whether to maximize or minimize
        the objective function.
        """
        self.problem = problem
        name = self.problem.__class__.__name__
        description = "Mathematical black-box function."
        target = Target(
            name="target",
            description="The value of the objective function.",
        )
        domain = "mathematics"
        parameters = []
        for i in range(self.problem.dim):
            p = Parameter(
                name=f"x_{i}",
                type=Type.continuous,
                description=f"The value of input variable {i}",
            )
            p.set_bounds(self.problem.lb[i], self.problem.ub[i])
            parameters.append(p)

        self.inverse = -1 if maximize else 1

        super().__init__(
            name=name,
            description=description,
            parameters=parameters,
            target=target,
            objective_function=self._get_objective_function(),
            domain=domain,
            xopt=self.problem.xopt,
            yopt=self.problem.yopt[0] * self.inverse,
        )

    @property
    def optimum(self):
        return (self.xopt, self.yopt)

    def _get_objective_function(self):

        def objective_function(x):
            res = self.problem(x) * self.inverse
            return res

        return objective_function
