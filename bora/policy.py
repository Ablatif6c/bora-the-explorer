import math
import numpy as np
from collections import deque
from enum import Enum
from typing import List


class Action(Enum):
    BO = 0
    ASSISTANT_SUGGESTS = 1
    ASSISTANT_SELECTS = 2

    def __str__(self):
        return self.name


class Policy:

    def __init__(
        self,
        dim: int,
        gamma: float = 0.05,
        m_init: float = None,
        trust_window_size: int = 3,
    ):
        """
        Initialize the Policy with the specified parameters.

        Parameters
        ----------
        dim : int
            The dimension of the optimization problem.

        gamma : float, optional
            The percentage by which the best found value must be increased.

        m_init : float, optional
            The initial plateau duration.

        trust_window_size : int, optional
            The size of the sliding window for trust calculation.
        """

        self.dim = dim
        self._gamma = gamma
        self._failures = 0
        self._previous_best_value = -np.inf
        self.current_action = Action.BO
        self._uncertainty = None
        self._lower_unc_threshold = None
        self._upper_unc_threshold = None
        self._uncertainties = []
        self._skip_update = False
        self._init_plateau_duration(m_init)
        self._trust_model = TrustModelSlidingWindow(window_size=trust_window_size)

    @property
    def plateau_duration(self):
        return self._plateau_duration

    @property
    def assistant_rolling_trust(self):
        return self._trust_model.get_rolling_trust()

    def _init_plateau_duration(self, m_init: float):
        self._plateau_duration = (
            math.ceil(2 * math.sqrt(self.dim)) if m_init is None else m_init
        )
        print(f"Plateau duration initialized to {self._plateau_duration}")
        self._plateau_lower_bound = 0
        self._plateau_upper_bound = 3 * self._plateau_duration
        self._max_delta = 15  # Maximum change in plateau duration per comment
        self._plateau_durations = [self._plateau_duration]

    def initialize(self, iteration: int, max_target: float, uncertainty: float):
        self._correct_uncertainty_bounds(iteration, uncertainty)
        self._previous_best_value = max_target

    def _correct_uncertainty_bounds(self, iteration: int, uncertainty: float):
        self._uncertainty = uncertainty
        self._uncertainties.append((iteration, self._uncertainty))
        max_uncertainty = max([uncertainty for _, uncertainty in self._uncertainties])
        self._upper_unc_threshold = 0.5 * max_uncertainty
        self._lower_unc_threshold = 0.3 * max_uncertainty

    def update(
        self,
        last_targets: List[float],
        max_target: float,
        iteration: int,
        uncertainty: float,
    ):
        """
        Update the failure count based on the performance of the last n
        probes.

        Parameters
        ----------
        n_last_probe : int
            The number of last probes to consider for updating the failure
            count.
        """
        # If the next action is forced, skip the update
        if self._skip_update:
            return

        # Get the maximum target value from the last n probes
        current_value = max(last_targets)

        # Update the failure count based on the current value and threshold
        threshold = self._get_improvement_threshold()
        if current_value >= threshold:
            # Reset failures if the current value meets or exceeds the
            # threshold
            self._failures = 0

        else:
            # Increment failures if the current value is below the threshold
            self._failures += 1

        # Update the trust model if the current action is not BO
        if self.current_action != Action.BO:
            self._trust_model.update(
                current_value, self._previous_best_value, iteration=iteration
            )
            self._adjust_plateau_duration(iteration)

        # Update the previous best value to the current maximum target value
        self._previous_best_value = max_target

        self._correct_uncertainty_bounds(iteration, uncertainty)

    def _get_improvement_threshold(self) -> float:
        """Determine the threshold based on the previous best value and gamma

        Returns
        --------
        threshold : float
            The improvement threshold.
        """
        threshold = None
        if self._previous_best_value >= 0:
            # If the previous best value is non-negative, increase it by gamma
            # percentage
            threshold = (1 + self._gamma) * self._previous_best_value
        else:
            # If the previous best value is negative, decrease it by gamma
            # percentage
            threshold = (1 - self._gamma) * self._previous_best_value
        return threshold

    def _adjust_plateau_duration(self, current_iteration: int):
        """Adjust plateau duration based on trust score."""
        current_trust = self._trust_model.get_rolling_trust()
        previous_trust = self._trust_model.get_previous_rolling_trust()
        diff = current_trust - previous_trust
        adjustment = diff * self._max_delta

        # Ensure the adjustment is within bounds
        # Not really needed as the max possible value of diff is 1
        # and adjustment is max_delta
        adjustment = max(-self._max_delta, adjustment)
        adjustment = min(self._max_delta, adjustment)

        # Update plateau duration
        self._plateau_duration -= adjustment

        # Ensure plateau duration is integer and within bounds
        self._plateau_duration = int(round(self._plateau_duration))
        self._plateau_duration = min(
            max(self._plateau_duration, self._plateau_lower_bound),
            self._plateau_upper_bound,
        )

        # Store the plateau duration for visualization
        self._plateau_durations.append((current_iteration, self._plateau_duration))

    def get_action(self) -> int:
        """
        Get the action to perform the optimization with.

        Returns
        --------
        Action : The action (BO or LLM ASSISTANT-based optimization).
        """
        if self._skip_update is True:
            self._skip_update = False
            self.current_action = Action.BO
            self._failures = 0
            return self.current_action

        if self._uncertainty < self._lower_unc_threshold:
            print(
                f"Uncertainty dropped below {self._lower_unc_threshold:.3f}. Continuing with standard BO"
            )
            self.current_action = Action.BO
            return self.current_action

        if (
            self.current_action == Action.ASSISTANT_SUGGESTS
            or self.current_action == Action.ASSISTANT_SELECTS
        ):
            self.current_action = Action.BO
            self._failures = 0
            return self.current_action

        elif self.current_action == Action.BO:
            if self._failures < self._plateau_duration:
                return self.current_action
            else:
                if self._uncertainty > self._upper_unc_threshold:
                    self.current_action = Action.ASSISTANT_SUGGESTS
                else:
                    self.current_action = Action.ASSISTANT_SELECTS
                return self.current_action

    def skip_next_update(self):
        self._skip_update = True


class TrustModelSlidingWindow:

    def __init__(self, window_size: int = 3):
        """
        Initialize the Trust Model with a specified sliding window size and
        sensitivity parameter.

        Parameters
        ---------
        window_size : int
            The number of recent iterations to consider for trust updating.
        """
        self.window_size = window_size
        self.performance_window = deque(maxlen=window_size)
        self._initial_trust_score = 0.9
        self.performance_window.append(self._initial_trust_score)
        self.iteration_rolling_trusts = []

    def calculate_score(self, y_t: float, y_best_previous: float) -> float:
        """
        Calculate the intervention score based on the magnitude of improvement.

        Parameters
        ---------
        y_t : float
            The current y value suggested by the LLM.
        y_best_previous : float
            The previous best y value before this iteration.

        Returns
        --------
        score intervention : float
            A value between 0 and 1 representing the utility of
            the LLM suggestion.
        """
        delta = y_t - y_best_previous
        if delta > 0:
            score_interv = 1.0
        else:
            norm_delta = delta / (abs(y_best_previous) + 1e-6)
            score_interv = 1.0 / (1.0 + np.exp(-1 * norm_delta))
        return score_interv

    def update(self, y_t: float, y_best_previous: float, iteration: int):
        """
        Update the trust model with the latest y_t and y_best_previous.

        Parameters
        ----------
        y_t : float
            The current y value suggested by the LLM.
        y_best_previous : float
            The previous best y value before this iteration.
        """
        score = self.calculate_score(y_t, y_best_previous)
        self.performance_window.append(score)
        self.iteration_rolling_trusts.append((iteration, self.get_rolling_trust()))

    def get_rolling_trust(self):
        """
        Calculate the average intervention scores over the sliding window.

        Returns
        -------
        rolling trust :float
            The average trust value between 0 and 1.
        """
        return np.mean(self.performance_window)

    def get_previous_rolling_trust(self):
        """
        Get the previous rolling trust.

        """
        if len(self.iteration_rolling_trusts) < 2:
            return self._initial_trust_score

        prev_rolling_trust_score = self.iteration_rolling_trusts[-2][1]
        return prev_rolling_trust_score
