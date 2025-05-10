import json
import os
import re
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """Read a CSV file and return a DataFrame."""
    data = pd.read_csv(file_path)

    # Process HypBO files
    if "HypBO" in file_path:
        save = False
        if "Unnamed" in str(data.columns[0]):
            data = data.rename(columns={data.columns[0]: "iteration"})
            save = True

        if "Target" in data.columns:
            data = data.rename(columns={"Target": "target"})
            save = True

        if len(data) > 105:
            # Keep the first 105 rows
            data = data.head(105)
            save = True

        if save:
            data.to_csv(file_path, index=False)

    # Process colabo files
    elif "ColaBO" in file_path and "arm_name" in data.columns:
        # Drop ["arm_name", "trial_status"]
        drops = ["trial_index", "arm_name", "trial_status"]
        new_cols = [c for c in data.columns if c not in drops]
        data = data[new_cols]

        # Put column ""generation_method" at the end in the dataframe
        data = data[[c for c in data.columns if c != "generation_method"] +
                    ["generation_method"]]

        # Get the target column which is the first column
        target_column_name = data.columns[0]

        # Rename it to "target"
        data = data.rename(columns={target_column_name: "target"})

        # Rename the index as iteration and make it start from 1
        data.index = range(1, len(data) + 1)
        data.index.name = "iteration"
        data.to_csv(file_path, index=True)

    # if the iteration column data starts from 0, make it start from 1
    # Make "iteration" the index if it is not
    if data.index.name != "iteration":
        data = data.set_index("iteration")
    if data.index[0] == 0:
        data.index = data.index + 1
        data.to_csv(file_path, index=True)
    return data


def process_targets(data: pd.DataFrame) -> pd.Series:
    """Process the targets column and return the best so far targets."""
    targets = data["target"]
    if "allowed" in data.columns:
        targets = targets.where(data["allowed"], 0)
    return targets.cummax()


def get_best_so_far_targets(file_path: str) -> List[str]:
    """Get the best so far targets from a CSV file."""
    data = read_csv(file_path)
    best_targets = process_targets(data)
    return best_targets.tolist()


def get_action_best_so_far_targets(file_path: str) -> List[str]:
    """Get the best so far targets of the actions from a CSV file."""
    data = read_csv(file_path)
    targets = data["target"]
    if "allowed" in data.columns:
        targets = targets.where(data["allowed"], 0)

    llm_targets = targets.where(data["hypotheses"].notna(), 0)
    # Get the first iteration where the hypotheses are not available
    first_na = None
    for i, row in data.iterrows():
        if pd.isna(row["hypotheses"]):
            first_na = i
            break
    vanilla_bo_targets = targets.where(data["hypotheses"].isna(),
                                       0)[first_na - 1:]

    # Cumulative max
    llm_target_bsf = llm_targets.cummax().tolist()
    vanilla_bo_target_bsf = [np.nan] * (
        first_na - 1) + vanilla_bo_targets.cummax().tolist()

    return llm_target_bsf, vanilla_bo_target_bsf


def get_data_files(data_folder: str, experiment_name: str) -> List[str]:
    """Get a list of data files matching the experiment name."""
    files = [
        file for file in os.listdir(data_folder)
        if os.path.isfile(os.path.join(data_folder, file))
        and re.search(rf'^data_{experiment_name}.*\d+\.csv$', file)
        and not file.startswith("summary")
    ]
    return files


def get_hypothesis_files(experiment_dir: str) -> List[str]:
    """Get a list of hypothesis files in the experiment directory."""
    files = [
        file for file in os.listdir(experiment_dir)
        if os.path.isfile(os.path.join(experiment_dir, file))
        and file.endswith("hypotheses.json")
    ]
    return files


def get_uncertainty_files(experiment_dir: str) -> List[str]:
    """Get a list of uncertainty files in the experiment directory."""
    files = [
        file for file in os.listdir(experiment_dir)
        if os.path.isfile(os.path.join(experiment_dir, file))
        and file.endswith("uncertainties.csv")
    ]
    return files


def extract_seed(file_name: str) -> int:
    """Extract the seed from the file name."""
    match = re.search(r's(\d+)\.csv', file_name)
    if match:
        return int(match.group(1))
    raise ValueError("Seed not found in file name.")


def extract_hypothesis_seed(file_name: str) -> int:
    """Extract the seed from the file name.

    Parameters
    ----------
    file_name : str
        The file name.

    Returns
    -------
    int
        The seed.
    """
    match = re.search(r's(\d+)\_hypotheses.json', file_name)
    if match:
        return int(match.group(1))
    raise ValueError("Seed not found in file name.")


def extract_uncertainty_seed(file_name: str) -> int:
    """Extract the seed from the file name.

    Parameters
    ----------
    file_name : str
        The file name.

    Returns
    -------
    int
        The seed.
    """
    match = re.search(r's(\d+)\_uncertainties.csv', file_name)
    if match:
        return int(match.group(1))
    raise ValueError("Seed not found in file name.")


def save_summary_file(
    data_folder: str,
    experiment_name: str,
    yopt: float,
) -> tuple:
    """
    Save a summary file with the mean and std of the best so far targets.

    Args:
        data_folder (str): The path to the data folder.
        experiment_name (str): The name of the experiment.

    Returns:
        tuple: A tuple containing the summary file path and the data.
    """
    data_files = get_data_files(data_folder, experiment_name)
    data = pd.DataFrame()

    seed_columns = []
    for file in data_files:
        seed = extract_seed(file)
        file_path = os.path.join(data_folder, file)
        best_targets = get_best_so_far_targets(file_path)
        data[seed] = best_targets
        seed_columns.append(seed)

    data.index = data.index + 1
    data.index.name = "iteration"
    data["mean_target"] = data.mean(axis=1)
    data["std_target"] = data.iloc[:, :-1].std(axis=1)

    # Regret
    # Calculate regret for each seed
    for seed in seed_columns:  # Exclude mean_target, std_target
        data[f"regret_{seed}"] = np.array(
            [yopt] * len(data[seed])) - data[seed]

    # Locate the regret columns and calculate the mean and std
    regret_cols = [f"regret_{seed}" for seed in seed_columns]
    data["mean_regret"] = data.loc[:, regret_cols].mean(axis=1)
    data["std_regret"] = data.loc[:, regret_cols].std(axis=1)

    # Cumulative regret
    for seed in seed_columns:
        data[f"cum_regret_{seed}"] = data[f"regret_{seed}"].cumsum()
    data["mean_cum_regret"] = data["mean_regret"].cumsum()
    data["std_cum_regret"] = data["std_regret"].cumsum()

    summary_file_path = os.path.join(
        data_folder,
        f"summary_{experiment_name}.csv",
    )
    data.to_csv(summary_file_path)
    return summary_file_path, data


def get_trust_scores_and_plateaus(file_path: str,
                                  n_init: int = 5
                                  ) -> Dict[int, Tuple[float, float]]:
    """Get the trust scores and plateau durations from a hypotheses file.

    Parameters
    ----------
    file_path : str
        The path to the hypotheses file.

    Returns
    -------
    dict
        A dictionary containing the trust scores and plateau durations.
    """
    data = json.load(open(file_path))
    metrics = {}
    for iteration in data:
        trust_score = data[iteration]["trust_score"]
        plateau_duration = data[iteration]["plateau_duration"]
        metrics[int(iteration)] = (trust_score, plateau_duration)

    # During BORA initialization, if the LLM fails to generate a random
    # point, it is replaced by a random sampled point, so the trust
    # score and plateau duration are set to "FAILED" in this case
    for i in range(1, n_init + 1):
        if i not in metrics:
            metrics[i] = ("FAILED", "FAILED")
    return metrics


def get_uncertainties(file_path: str) -> Dict[int, float]:
    """Get the uncertainties from an uncertainty file.

    Parameters
    ----------
    file_path : str
        The path to the uncertainty file.

    Returns
    -------
    list
        A list of uncertainties.
    """
    data = read_csv(file_path)
    res = {}
    for i in range(1, 106):
        if i < 6:
            res[int(i)] = np.nan
        else:
            uncertainty = float(
                data.loc[i, "uncertainty"]) if i in data.index else np.nan
            res[int(i)] = uncertainty
    return res


def save_bora_metrics_summary_file(
        experiment_dir: str,
        experiment_name: str,
        n_init: int = 5) -> Tuple[str, pd.DataFrame]:
    """
    Save a summary file with the BORA metrics.

    Parameters
    ----------
    experiment_dir : str
        The path to the data directory.
    experiment_name : str
        The name of the experiment.

    Returns
    -------
    Tuple[str, pd.DataFrame]
        A tuple containing the summary file path and the data.
    """
    hypothesis_files = get_hypothesis_files(experiment_dir)
    data = pd.DataFrame({"iteration": range(1, 106)}).set_index("iteration")
    seeds = []

    for h_file in hypothesis_files:
        seed = extract_hypothesis_seed(h_file)
        seeds.append(seed)
        file_path = os.path.join(experiment_dir, h_file)
        res = get_trust_scores_and_plateaus(file_path, n_init=n_init)
        trust_scores, plateau_durations = zip(
            *[res.get(i, (np.nan, np.nan)) for i in range(1, 106)])
        data[f"trust_score_{seed}"] = trust_scores
        data[f"plateau_duration_{seed}"] = plateau_durations

    trust_score_data, plateau_duration_data = interpolate_metrics(
        data, seeds, ["trust_score", "plateau_duration"])
    data["mean_trust_score"], data["std_trust_score"] = np.mean(
        trust_score_data, axis=0), np.std(trust_score_data, axis=0)
    data["mean_plateau_duration"], data["std_plateau_duration"] = np.mean(
        plateau_duration_data, axis=0), np.std(plateau_duration_data, axis=0)

    uncertainty_files = get_uncertainty_files(experiment_dir)
    for file in uncertainty_files:
        seed = extract_uncertainty_seed(file)
        file_path = os.path.join(experiment_dir, file)
        uncertainties = get_uncertainties(file_path)
        data[f"uncertainty_{seed}"] = list(uncertainties.values())

    data_uncertainties = interpolate_uncertainties(data, seeds)
    data["mean_uncertainty"] = np.hstack(
        [np.array([np.nan] * 5),
         np.mean(data_uncertainties, axis=0)])
    data["std_uncertainty"] = np.hstack(
        [np.array([np.nan] * 5),
         np.std(data_uncertainties, axis=0)])

    # Reorder columns
    ordered_columns = []
    for metric in ["trust_score", "plateau_duration", "uncertainty"]:
        for seed in seeds:
            ordered_columns.append(f"{metric}_{seed}")
        ordered_columns.extend([
            f"mean_{metric}",
            f"std_{metric}",
        ])

    data = data[ordered_columns]
    summary_file_path = os.path.join(
        experiment_dir, f"summary_bora_metrics_{experiment_name}.csv")
    data.to_csv(summary_file_path)
    return summary_file_path, data


def interpolate_metrics(data, seeds, metrics):
    interpolated_data = {metric: [] for metric in metrics}
    for seed in seeds:
        for metric in metrics:
            iterations_trial = [
                i for i in data.index
                if data.loc[i, f"{metric}_{seed}"] != "FAILED"
                and not np.isnan(data.loc[i, f"{metric}_{seed}"])
            ]
            metric_values_trial = data.loc[iterations_trial,
                                           f"{metric}_{seed}"].values.tolist()
            interp_trial = np.interp(data.index, iterations_trial,
                                     metric_values_trial)
            interpolated_data[metric].append(interp_trial)
    return interpolated_data["trust_score"], interpolated_data[
        "plateau_duration"]


def interpolate_uncertainties(data, seeds):
    data_uncertainties = []
    for seed in seeds:
        iterations_trial = data.index[
            data[f"uncertainty_{seed}"].notna()].tolist()
        uncertainties_trial = data.loc[iterations_trial,
                                       f"uncertainty_{seed}"].values.tolist()
        interp_trial = np.interp(data.index[5:], iterations_trial,
                                 uncertainties_trial)
        data_uncertainties.append(interp_trial)
    return data_uncertainties


def save_summary_actions_file(
        experiment_data_dir: str,
        experiment_name: str) -> Tuple[str, pd.DataFrame]:
    """
    Save a summary file with the mean and std of the best so far targets from
    the actions.

    Parameters:
    ----------
        experiment_data_dir (str): The path to the data folder.
        experiment_name (str): The name of the experiment.

    Returns
    -------
        Tuple[str, pd.DataFrame]: A tuple containing the summary file path and the data.
    """
    data_files = get_data_files(experiment_data_dir, experiment_name)
    data = pd.DataFrame()

    seed_columns = []
    for file in data_files:
        seed = extract_seed(file)
        file_path = os.path.join(experiment_data_dir, file)
        llm_bsf, vanilla_bo_bsf = get_action_best_so_far_targets(file_path)
        data[f"{seed}_llm"] = llm_bsf
        data[f"{seed}_vanilla_bo"] = vanilla_bo_bsf
        seed_columns.append(seed)

    data.index = data.index + 1
    data.index.name = "iteration"

    cols = [f"{seed}_llm" for seed in seed_columns]
    data["mean_target_llm"] = data[cols].mean(axis=1)
    data["std_target_llm"] = data[cols].std(axis=1)

    cols = [f"{seed}_vanilla_bo" for seed in seed_columns]
    data["mean_target_vanilla_bo"] = data[cols].mean(axis=1)
    data["std_target_vanilla_bo"] = data[cols].std(axis=1)

    # Save the summary file
    summary_file_path = os.path.join(
        experiment_data_dir,
        f"summary_{experiment_name}_actions.csv",
    )
    data.to_csv(summary_file_path, index=True)

    return summary_file_path, data


def get_bora_experiment_cost(experiment_dir: str) -> float:
    # Get the price files
    price_files = [
        file for file in os.listdir(experiment_dir)
        if os.path.isfile(os.path.join(experiment_dir, file))
        and file.endswith("_price.txt")
    ]

    # Get the total cost
    total_cost = 0
    for file in price_files:
        file_path = os.path.join(experiment_dir, file)
        with open(file_path, "r") as f:
            price = f.read().split("$")[0]
            price = float(price)
        total_cost += price

    return total_cost


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(
        os.path.dirname(current_dir),
        "data",
    )
    experiment = "Photocatalytic Hydrogen Production_d10"
    experiment_data_dir = os.path.join(data_dir, experiment, "BORA")
    cost = get_bora_experiment_cost(experiment_data_dir)
