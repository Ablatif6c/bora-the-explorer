"""
This script is to do some batch testing with a few experiments

It saves the optimization data in the specified folder path.
"""

import os
import argparse
from bora.bora import Bora
from utils import get_experiment_from_name

# Initialize parser
parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument(
    "-e",
    "--experiment",
    help="Experiment",
    type=str,
    default="Greenhouse Biomass Production",
)
parser.add_argument(
    "-d",
    "--dim",
    help="Experiment dimension. Automatically inferred for the real-world experiments.",
    type=int,
    default=8,
)
parser.add_argument(
    "-n",
    "--n_init",
    help="Number of iterations before the optimization starts.",
    type=int,
    default=5,
)
parser.add_argument(
    "-N",
    "--n_iter",
    help="Number of iterations where the method attempts to find the optimum.",
    type=int,
    default=20,
)

parser.add_argument(
    "-llm",
    "--llm_model",
    help="The OpenAI language model to use.",
    type=str,
    default="gpt-4o-mini",
)
parser.add_argument(
    "-api",
    "--api_key",
    help="The OpenAI API key.",
    type=str,
    default="",
)
parser.add_argument(
    "-ss",
    "--seed_start",
    help="The starting seed for the experiments.",
    type=int,
    default=0,
)
parser.add_argument(
    "-se",
    "--seed_end",
    help="The ending seed for the experiments.",
    type=int,
    default=1,
)
parser.add_argument(
    "-m",
    "--m_init",
    help="The initial plateau duration. Default is automatically set.",
    type=float,
    default=None,
)
parser.add_argument(
    "-as",
    "--ablation_studies",
    help="Whether this is an ablation study run.",
    action="store_true",
    default=False,
)
args = parser.parse_args()


def get_data_dir(data_dir: str) -> str:
    """
    Set the experiment data directory based on whether it is an ablation
    study.

    Parameters
    ----------
        data_dir (str): The data directory.

    Returns
    -------
        str: The updated experiment data directory.
    """
    # Set the data directory based on whether it is an ablation study
    if args.ablation_studies:
        data_dir = os.path.join(data_dir, "ablation_studies")
    else:
        data_dir = os.path.join(data_dir, "main_results")

    # Create the directory if it does not exist
    os.makedirs(data_dir, exist_ok=True)

    return data_dir


def get_experiment_data_dir(data_dir: str, experiment_name: str, dim) -> str:
    model = f"BORA_m_init_{args.m_init}" if args.ablation_studies else "BORA"
    experiment_data_dir = os.path.join(data_dir, f"{experiment_name}_d{dim}", model)
    os.makedirs(experiment_data_dir, exist_ok=True)
    return experiment_data_dir


def optimize_experiment(random_seed: int, data_dir: str = "data"):
    """
    Optimize the experiment with the given random seed.

    Parameters
    ----------
    random_seed : int
        The random seed for the experiment.

    data_dir : str, optional (default="data")
        The folder to save the data.
    """
    # Get the API key
    api_key = os.getenv("OPENAI_API_KEY") if args.api_key == "" else args.api_key
    if api_key == "":
        raise ValueError("OPENAI API key is not set.")

    # Get the experiment
    experiment = get_experiment_from_name(
        args.experiment,
        args.dim,
        random_seed,
    )

    data_dir = get_data_dir(data_dir)
    experiment_data_dir = get_experiment_data_dir(
        data_dir, args.experiment, experiment.dim
    )

    print(
        f"\nOptmimizing {args.experiment}_d{experiment.dim}\t"
        + f"Seed: {random_seed}/{args.seed_end-1}\t Assistant: {args.llm_model}"
    )

    log_path = os.path.join(
        experiment_data_dir,
        f"comments_{args.experiment}_d{experiment.dim}_s{random_seed}.md",
    )

    # Run the optimization
    bora = Bora(
        experiment=experiment,
        llm_model=args.llm_model,
        api_key=api_key,
        log_path=log_path,
        random_seed=random_seed,
        m_init=args.m_init,
        save_prompts=True,
    )
    bora.maximize(n_init_points=args.n_init, n_iter=args.n_iter)
    print(f"\nThe max found is: {bora.max}")

    # Save the results
    bora.save_data(experiment_data_dir)


if __name__ == "__main__":
    for i in range(args.seed_start, args.seed_end):
        optimize_experiment(i)
