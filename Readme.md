# Language-Based Bayesian Optimization Research Assistant (BORA)

## Overview

This repository contains the source code and associated materials for the BORA algorithm from the **_Language-Based Bayesian Optimization Research Assistant (BORA)_** paper appearing in IJCAI 2025. This codebase allows for the replication of the experiments and findings presented in the paper.

Many important scientific problems involve multivariate optimization coupled with slow and laborious experimental measurements. These complex, high-dimensional searches can be defined by non-convex optimization landscapes that resemble needle-in-a-haystack surfaces, leading to entrapment in local minima. Contextualizing optimizers with human domain knowledge is a powerful approach to guide searches to localized fruitful regions. However, this approach is susceptible to human confirmation bias and it is also challenging for domain experts to keep track of the rapidly expanding scientific literature. Here, we propose the use of Large Language Models (LLMs) for contextualizing Bayesian optimization (BO) via a hybrid optimization framework that intelligently and economically blends stochastic inference with domain knowledge-based insights from the LLM, which is used to suggest new, better-performing areas of the search space for exploration. Our method fosters user engagement by offering real-time commentary on the optimization progress, explaining the reasoning behind the search strategies. We validate the effectiveness of our approach on synthetic benchmarks with up to 15 independent variables and demonstrate the ability of LLMs to reason in four real-world experimental tasks where context-aware suggestions boost optimization performance substantially.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Citation](#citation)
- [License](#license)

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. First, make sure you have Python3.11.8 installed on your machine. If not, you can download it from the [Python website](https://www.python.org/downloads/).
2. Open a terminal or command prompt.
3. Navigate to the bora-the-explorer directory where to create the virtual environment. You can do this with the `cd` command by typing `cd bora-the-explorer`.
4. Once you're in the directory, you can create the virtual environment with the `python -m venv` command by running `python3.11.8 -m venv .venv`.
5. After the virtual environment is created, you can activate it. The command to do this depends on your operating system:
   - On Windows, type `.venv\Scripts\activate`.
   - On Unix or MacOS, type `source .venv/bin/activate`.
6. Once the `.venv` virtual environment is activated, your terminal or command prompt should show the name of the virtual environment.
7. You can now install the required packages into the `.venv` virtual environment using `pip install -r requirements.txt`.

## Usage

Note that BORA is a maximizing optimizer. Please make sure you reformulate potential minimization problems.
The experiments can be run from `main.py`.

### Synthetic Functions

The synthetic function for testing optimization algorithms are taken from the [Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html) and implemented in the `experiments/synthetic` folder where you will find an exhaustive list of those synthetic functions.

### Real-world Benchmarks

The real-world benchmarks can be consulted in `experiments/real_world` folder.

## Citation

Please cite us as:

```
@inproceedings{cisse2025bora,
  title = {Language-Based Bayesian Optimization Research Assistant (BORA)},
  author = {Cisse, Abdoulatif and Evangelopoulos, Xenophon and Gusev, Vadimir V and Cooper, Andrew I},
  booktitle = {Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence, {IJCAI-25}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  year      = {2025},
  note      = {Main Track}
}
```

An extended version of the paper which includes the Supplementary Material can be found at [arXiv:2501.16224](https://arxiv.org/abs/2501.16224).

## License

[MIT license](https://opensource.org/license/mit/)
