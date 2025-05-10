"""
This script virtualizes the Photocatalytic Hydrogen Production from the
extended experimental data provided by the authors of 'A Mobile Robotic
Chemist'. This data is saved as 'her_data.csv' in this folder. The script
trains a Gaussian Process model on this data and saves the model in this
current folder as 'her_model.pkl'.

Bibtex of the 'A Mobile Robotic Chemist' paper:
@article{c:MobileRoboticChemist,
    title={A mobile robotic chemist},
    author={Benjamin Burger and Phillip M. Maffettone and Vladimir V. Gusev
    and Catherine M. Aitchison and Yang Bai and Xiao-yan Wang and Xiaobo Li
    and Ben M. Alston and Buyin Li and Rob Clowes and Nicola Rankin and
    Brandon Harris and Reiner Sebastian Sprick and Andrew I. Cooper},
    journal={Nature},
    year={2020},
    volume={583},
    pages={237-241},
    url={https://api.semanticscholar.org/CorpusID:220420261}
}
"""

import os
import pickle
from typing import Tuple

import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import (ConstantKernel, Matern,
                                              WhiteKernel)


def get_exp_data(data_path: str) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Get the extended experimental data from the 'A Mobile Robotic
    Chemist' paper.

    Parameters
    ----------
    data_path: str
        Path to the extended experimental data.

    Returns
    -------
    X: pd.DataFrame
        Features
    Y: pd.Series
        Target
    """
    data = pd.read_csv(data_path)
    X = data.iloc[:, :10]  # Features
    Y = data.iloc[:, -1]  # Target

    return X, Y


print("Building the model for the Hydrogen Production experiment...")
# ---------------------- Get the experimental data ----------------------
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "her_data.csv")
X_train, Y_train = get_exp_data(data_path)

# -----------------------------Train the model --------------------------
# The initial length scales correspond to the feature discretization
length_scale = [0.25, 0.25, 0.25, 0.25, 0.25, 0.2, 0.25, 0.25, 0.25, 0.25]

# The kernel is a Matern kernel with nu=2.5, a constant kernel and a white
# noise kernel
kernel = Matern(length_scale=length_scale,
                length_scale_bounds=(1e-01, 1e4),
                nu=2.5)
kernel *= ConstantKernel(1.0, (0.5, 5))
kernel += WhiteKernel(noise_level=0.1, noise_level_bounds=(5e-02, 7e-1))

# Initialize the model
dim = X_train.shape[1]
random_state = 1
model = GaussianProcessRegressor(
    kernel=kernel,
    alpha=1e-6,
    normalize_y=False,
    n_restarts_optimizer=10 * dim,
    random_state=random_state,
)

# Train the model
start_time = pd.Timestamp.now()
print("Training the model...")
model.fit(X=X_train, y=Y_train)
end_time = pd.Timestamp.now()
print(f"Training time: {end_time - start_time}")

# Save the model
model_path = os.path.join(current_dir, "her_model.pkl")
with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model saved at: {model_path}")
