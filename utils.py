import inspect

from bora.experiment import Experiment
from experiments.real_world.biomass_production.biomass_production import \
    GreenhouseBiomassProduction
from experiments.real_world.hydrogen_production.hydrogen_production import \
    PhotocatalyticHydrogenProduction
from experiments.real_world.projectile.projectile import Projectile
from experiments.real_world.solar_energy_production.solar_energy_production import \
    SolarEnergyProduction
from experiments.synthetic import standard_test_functions as fcts
from experiments.synthetic.test_problem import TestProblem


def get_experiment_from_name(
    name: str,
    dim: int = 5,
    random_seed: int = 0,
) -> Experiment:
    """
    Returns the Experiment object. Synthetic experiments are retrieved
    from 'standard_test_problems.py' which take a dimension parameter in a
    dictionary form. Real-world experiments are retrieved from the 'real_world'
    subfolder.

    Parameters
    ----------
    name : str
        Name of the function.
    dim :  int, optional (default=5)
        Dimension of the function.
    random_seed : int, optional (default=0)
        Random seed for the experiment.

    Returns
    -------
    Experiment : The experiment object.
    """
    experiment = None

    #  Real-world experiments
    if name == "Photocatalytic Hydrogen Production":
        experiment = PhotocatalyticHydrogenProduction(random_seed=random_seed)
    elif name == "Greenhouse Biomass Production":
        experiment = GreenhouseBiomassProduction()
    elif name == "Solar Energy Production":
        experiment = SolarEnergyProduction()
    elif name == "Projectile":
        experiment = Projectile()

    # Synthetic functions. Note that the synthetic functions, because their
    # dimensionality can be changed at will, do not use experiment cards in
    # the default sense as the real-world experiments. Instead they are
    # automatically directly instantiated from the standard_test_functions.py
    # file.
    else:
        # Get the function from the standard_test_functions.py file.
        members = inspect.getmembers(fcts)
        for f_name, f in members:
            f_args = inspect.signature(f.__init__).parameters
            if inspect.isclass(f) and f_name != "TestProblem":
                if f_name.lower() == name.lower():
                    test_problem = None
                    # If the function takes a dimension parameter.
                    if "d" in f_args:
                        test_problem = TestProblem(
                            problem=f(d=dim),
                            maximize=True,
                        )
                    else:
                        test_problem = TestProblem(
                            problem=f(),
                            maximize=True,
                        )
                    experiment = test_problem
                    break
                else:
                    continue
        if not experiment:
            raise ValueError(f"Experiment '{name}' not found!")

    return experiment
