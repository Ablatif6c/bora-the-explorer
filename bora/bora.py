"""Main module.

Holds the `BORA` class, which handles the maximization of a
function over a specific target space with LLM interventions.
"""

import json
import os
import warnings
import numpy as np
import pandas as pd
from copy import deepcopy
from typing import List
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from .acquisition import AcquisitionFunction, ExpectedImprovement
from .assistant import Assistant
from .event import DEFAULT_EVENTS, Events
from .experiment import Experiment
from .logger import _get_default_logger
from .policy import Action, Policy
from .target_space import Space, TargetSpace
from .util import ensure_rng, hashable


class Queue:
    """Queue data structure.

    Append items in the end, remove items from the front.
    """

    def __init__(self):
        self._queue = []

    @property
    def empty(self):
        """Check whether the queue holds any items."""
        return len(self) == 0

    def __len__(self):
        """Return number of items in the Queue."""
        return len(self._queue)

    def __next__(self):
        """Remove and return first item in the Queue."""
        if self.empty:
            raise StopIteration("Queue is empty, no more objects to retrieve.")
        obj = self._queue[0]
        self._queue = self._queue[1:]
        return obj

    def add(self, obj):
        """Add object to end of queue."""
        self._queue.append(obj)


class Observable:
    """Inspired by
    https://www.protechtraining.com/blog/post/879#simple-observer."""

    def __init__(self, events):
        """
        Maps event names to subscribers

        Parameters
        ----------
        events : list
            List of events to track.
        """
        self._events = {event: dict() for event in events}

    def get_subscribers(self, event):
        """
        Return the subscribers of an event.

        Parameters
        ----------
        event : str
            The event to get subscribers for.
        """
        return self._events[event]

    def subscribe(self, event, subscriber, callback=None):
        """
        Add subscriber to an event.

        Parameters
        ----------
        event : str
            The event to subscribe to.

        subscriber : object
            The subscriber to add.

        callback : function, optional
            The callback function to use.
        """
        if callback is None:
            callback = getattr(subscriber, "update")
        self.get_subscribers(event)[subscriber] = callback

    def unsubscribe(self, event, subscriber):
        """
        Remove a subscriber for a particular event.

        Parameters
        ----------
        event : str
            The event to unsubscribe from.

        subscriber : object
            The subscriber to remove.
        """
        del self.get_subscribers(event)[subscriber]

    def dispatch(self, event, *args, **kwargs):
        """Trigger callbacks for subscribers of an event."""
        for _, callback in self.get_subscribers(event).items():
            callback(event, self, *args, **kwargs)


class Bora(Observable):

    def __init__(
        self,
        experiment: Experiment,
        api_key: str,
        log_path: str,
        llm_model: str = "gpt-4o-mini",
        verbose: bool = True,
        allow_duplicate_points: bool = False,
        acquisition_function=None,
        bounds_transformer=None,
        gamma: float = 0.05,
        m_init: float = None,
        trust_window_size: int = 3,
        random_seed: int = 0,
        save_prompts: bool = False,
    ):
        """
        Parameters
        ----------
        experiment : Experiment
            The experiment to optimize.

        api_key : str
            The API key for the assistant.

        llm_model : str, optional (default="gpt-4o-mini")
            The LLM model to use.

        log_path : str
            The path to save the logs in markdown.

        verbose : bool, optional (default=True)
            Whether to print the logs.

        allow_duplicate_points : bool, optional (default=False)
            Whether to allow duplicate points.

        acquisition_function : AcquisitionFunction, optional (default=None)
            The acquisition function to use.

        bounds_transformer : DomainTransformer, optional (default=None)
            The bounds transformer to use.

        gamma : float, optional (default=0.05)
            The gamma parameter for the policy.

        m_init : float, optional (default=None)
            The initial value for the plateau duration. If None, it is set to
            ceil(2 * sqrt(dim)).

        trust_window_size : int, optional (default=3)
            The trust window size for the policy.

        random_seed : int, optional (default=0)
            The random seed to use.

        save_prompts : bool, optional (default=False)
            Whether to save the prompts.
        """
        self._random_state = ensure_rng(random_seed)
        self._allow_duplicate_points = allow_duplicate_points
        self._experiment = experiment
        self._queue = Queue()
        self._gp = self._init_gp()
        self._space = self._init_target_space(random_seed)
        self._acquisition_function = self._init_acquisition_function(
            acquisition_function
        )
        self._assistant = self._init_assistant(
            api_key=api_key,
            log_path=log_path,
            llm_model=llm_model,
            random_seed=random_seed,
            save_prompts=save_prompts,
        )
        self._policy = Policy(self._experiment.dim, gamma, m_init, trust_window_size)
        self._uncertainty_points = self._space.random_points(5000)
        self._hypothesis_names = []
        self._hypothesis_records = {}
        self._verbose = verbose

        self._bounds_transformer = bounds_transformer
        self._init_bounds_transformer()

        super(Bora, self).__init__(events=DEFAULT_EVENTS)

    @property
    def space(self):
        """Return the target space associated with the optimizer."""
        return self._space

    @property
    def is_constrained(self):
        """Check whether the optimizer is constrained."""
        return self._experiment.constraint is not None

    @property
    def constraint(self):
        """Return the constraint associated with the optimizer, if any."""
        if self.is_constrained:
            return self._space.constraint
        return None

    @property
    def max(self):
        """Get maximum target value found and corresponding parameters.

        See `TargetSpace.max` for more information.
        """
        return self._space.max()

    @property
    def res(self):
        """Get all target values and constraint fulfillment for all parameters.

        See `TargetSpace.res` for more information.
        """
        return self._space.res()

    def _init_gp(self):
        """
        Initialize the Gaussian Process Regressor.

        Returns
        --------
        GaussianProcessRegressor: The Gaussian Process Regressor to use.
        """
        gp = GaussianProcessRegressor(
            kernel=Matern(nu=2.5),
            alpha=1e-6,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=self._random_state,
        )

        return gp

    def _init_target_space(self, random_seed: int) -> Space:
        """
        Initialize the target space.

        Parameters
        ----------
        random_seed : int
            The random seed to use.

        Returns
        --------
        Space: The target space.
        """
        if self._experiment.constraint is None:
            space = TargetSpace(
                self._experiment,
                pbounds=self._experiment.pbounds,
                key_order=self._experiment.keys,
                random_state=random_seed,
                allow_duplicate_points=self._allow_duplicate_points,
                discretization_steps=self._experiment.get_discretization_steps(),
            )
            return space
        else:
            space = TargetSpace(
                self._experiment,
                pbounds=self._experiment.pbounds,
                key_order=self._experiment.keys,
                constraint=self._experiment.constraint.constraint,
                random_state=random_seed,
                allow_duplicate_points=self._allow_duplicate_points,
                discretization_steps=self._experiment.get_discretization_steps(),
            )
            return space

    def _init_assistant(
        self,
        api_key: str,
        log_path: str,
        llm_model: str,
        random_seed: int,
        save_prompts: bool,
    ) -> Assistant:
        """
        Initialize the LLM assistant.

        Parameters
        ----------
        api_key : str
            The API key for the assistant.

        log_path : str
            The path to save the logs in markdown.

        llm_model : str
            The LLM model to use.

        random_seed : int
            The random seed to use.

        save_prompts : bool
            Whether to save the prompts.

        Returns
        --------
        Assistant: The assistant to use.
        """

        random_point = self._space.random_points(1)[0]
        assistant = Assistant(
            api_key=api_key,
            experiment=self._experiment,
            random_point=random_point,
            log_path=log_path,
            llm_model=llm_model,
            allow_duplicate_points=self._allow_duplicate_points,
            random_seed=random_seed,
            save_prompts=save_prompts,
        )
        return assistant

    def _init_acquisition_function(
        self, acquisition_function: AcquisitionFunction
    ) -> AcquisitionFunction:
        """
        Initialize the acquisition function.

        Parameters
        ----------
        acquisition_function : AcquisitionFunction
            The acquisition function to use.

        Returns
        --------
        AcquisitionFunction: The acquisition function to use.
        """
        if acquisition_function is None:
            return ExpectedImprovement(xi=0.01, random_state=self._random_state)
        return acquisition_function

    def _init_bounds_transformer(self):
        """
        Initialize the bounds transformer.
        """
        if self._bounds_transformer:
            try:
                self._bounds_transformer.initialize(self._space)
            except (AttributeError, TypeError):
                raise TypeError(
                    "The transformer must be an instance of DomainTransformer"
                )

    def _prime_subscriptions(self):
        """
        Add default subscriptions.
        """
        if not any([len(subs) for subs in self._events.values()]):
            _logger = _get_default_logger(
                self._verbose,
                self.is_constrained,
                None,
                default_precision=self._experiment.default_precision,
            )
            self.subscribe(Events.OPTIMIZATION_START, _logger)
            self.subscribe(Events.OPTIMIZATION_STEP, _logger)
            self.subscribe(Events.OPTIMIZATION_END, _logger)
            self.subscribe(Events.COMMENT_START, _logger)
            self.subscribe(Events.COMMENT_STEP, _logger)
            self.subscribe(Events.COMMENT_END, _logger)

    def _initialize_queue(
        self,
        n_init_points: int,
    ):
        """Ensure the queue is not empty. If it is, add random points.

        Parameters
        ----------
        n_init_points: int
            Number of initial points to add to the queue.
        """
        # Prepare the cache
        cache = deepcopy(self._space._cache)

        # Add existing points to cache to avoid duplicates
        for p in self._queue._queue:
            cache[hashable(p)] = None

        # If the queue is empty, we need to add at least 2 points
        if self._queue.empty and self._space.empty:
            n_init_points = max(n_init_points, 2)

        # Get the points from the assistant through the pre-optimization comment
        comment = self._assistant.pre_optimization_comment(
            n_hypotheses=n_init_points,
        )

        # Add the points from the comment
        if comment is not None and comment.is_valid:
            iteration = 1
            for h in comment.hypotheses:
                for p in h["points"]:
                    p = self._space.params_to_array(p)
                    self._queue.add(p)
                    self._hypothesis_names.append(h["name"])
                    cache[hashable(p)] = None
                    n_init_points -= 1

                    # Tracking
                    self._hypothesis_records[iteration] = {
                        "trust_score": self._policy.assistant_rolling_trust,
                        "plateau_duration": self._policy.plateau_duration,
                        "hypothesis": h,
                        "point": "[" + ", ".join(map(str, p)) + "]",
                    }
                    iteration += 1

                    if n_init_points == 0:
                        return

        # Add the remaining samples from random sampling
        points = self._space.random_points(n_init_points, cache)
        for point in points:
            self._queue.add(point)
            self._hypothesis_names.append("None")

            # Tracking
            self._hypothesis_records[iteration] = {
                "trust_score": "FAILED",
                "plateau_duration": "FAILED",
                "hypothesis": "FAILED",
                "point": "FAILED",
            }

    def _get_next_probe_list(self) -> List[List[float]]:
        """
        Get the next probe list.

        Returns
        --------
        List[List[float]]: The next probe list.
        """
        # If the queue is not empty, return the next probe list
        try:
            return [next(self._queue)]
        # If the queue is empty, suggest a new probe list
        except StopIteration:
            self._hypothesis_names = []
            suggestions = []
            action = self._policy.get_action()
            if action == Action.ASSISTANT_SUGGESTS:
                suggestions = self._get_assistant_suggestions()
            elif action == Action.ASSISTANT_SELECTS:
                suggestions = self._get_assistant_selections()
            else:
                suggestions = self._get_bo_suggestions()
            return suggestions

    def _get_bo_suggestions(self) -> List[List[float]]:
        """
        Get the next suggestions from the Bayesian optimization.

        Returns
        -------
        List[List[float]] : The next suggestions from the BO.
        """
        x_probe_list = self.suggest(n=1)
        self._hypothesis_names = ["None"]
        return x_probe_list

    def _get_assistant_suggestions(self) -> List[List[float]]:
        """
        Get the next suggestions from the assistant.

        Returns
        -------
        List[List[float]] : The next suggestions from the assistant.
        """
        data_so_far = self._get_data_so_far()
        print(f"Plateau of {self._policy.plateau_duration} detected")
        print(f"Action: {Action.ASSISTANT_SUGGESTS}")

        cache = self._get_cache()
        comment = self._assistant.comment_optimization(data_so_far, cache)
        x_probe_list = self._process_comment(
            comment=comment, next_iteration=len(data_so_far) + 1
        )
        return x_probe_list

    def _get_assistant_selections(self) -> List[List[float]]:
        """
        Get the next suggestions from the assistant.

        Returns
        -------
        List[List[float]] : The next suggestions from the assistant.
        """
        data_so_far = self._get_data_so_far()
        print(f"Plateau of {self._policy.plateau_duration} detected")
        print(f"Action: {Action.ASSISTANT_SELECTS}")
        # Get 5 points from the global optimization
        suggestions = self.suggest(5)
        suggestions = pd.DataFrame(
            suggestions, columns=self._space.keys
        ).drop_duplicates()
        comment = self._assistant.comment_and_select_point(data_so_far, suggestions)

        x_probe_list = self._process_comment(
            comment=comment, next_iteration=len(data_so_far) + 1
        )
        return x_probe_list

    def _process_comment(self, comment, next_iteration: int):
        # Retrieving the point suggestions from the comment.
        if comment is not None and comment.is_valid:
            self.dispatch(Events.COMMENT_STEP)

            # Get the points
            x_probe_list = []
            iteration = comment.iteration
            self._hypothesis_names = []
            for hypothesis in comment.hypotheses:
                for p in hypothesis["points"]:
                    if iteration > self.budget:
                        break
                    p = self._space.params_to_array(p)
                    x_probe_list.append(p)

                    self._hypothesis_names.append(hypothesis["name"])
                    self._hypothesis_records[iteration] = {
                        "trust_score": self._policy.assistant_rolling_trust,
                        "plateau_duration": self._policy.plateau_duration,
                        "hypothesis": hypothesis,
                        "point": "[" + ", ".join(map(str, p)) + "]",
                    }
                    iteration += 1

            self.dispatch(Events.OPTIMIZATION_START)

            return x_probe_list
        else:
            # If the comment is not valid, suggest a point accordingly
            # from the global optimization
            print("Assistant failed to comment. Reverting to standard BO")
            x_probe_list = self.suggest(n=1)
            self._hypothesis_names = ["None"]

            # Skip next update and record failure
            self._policy.skip_next_update()
            self._hypothesis_records[next_iteration] = {
                "trust_score": "FAILED",
                "plateau_duration": "FAILED",
                "hypothesis": "FAILED",
                "point": "FAILED",
            }

            return x_probe_list

    def _get_data_so_far(self) -> pd.DataFrame:
        """
        Get the optimization data so far.

        Returns
        --------
        pd.DataFrame: The optimization data gathered so far.
        """
        # Prepare the columns
        columns = ["Iteration"] + self._space.keys + [self._experiment.target.name]

        # Get the corresponding data
        data = []
        for i, (params, target) in enumerate(
            zip(self._space.params, self._space.target)
        ):
            data.append([i + 1] + list(params) + [target])
        data = pd.DataFrame(data, columns=columns)

        return data

    def _get_cache(self) -> dict:
        """
        Get the cache of the optimization data.

        Returns
        --------
            dict: The cache of the optimization data.
        """
        cache = deepcopy(self._space._cache)
        return cache

    def _get_mean_uncertainty(self) -> float:
        """
        Get the mean uncertainty of the target values.

        Returns:
        -------
        float: The mean uncertainty of the target values.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self._gp.fit(self._space.params, self._space.target)
            if self._space.constraint is not None:
                self._space.constraint.fit(
                    self._space.params, self._space._constraint_values
                )

        uncertainties = self._gp.predict(self._uncertainty_points, return_std=True)[1]
        mean_uncertainty = np.mean(uncertainties)
        return mean_uncertainty

    def set_bounds(self, new_bounds):
        """
        Modify the bounds of the search space.

        Parameters
        ----------
        new_bounds : dict
            A dictionary with the parameter name and its new bounds
        """
        self._space.set_bounds(new_bounds)

    def set_gp_params(self, **params):
        """Set parameters of the internal Gaussian Process Regressor."""
        self._gp.set_params(**params)
        self.hypotheses = [h._gp.set_gp_params(**params) for h in self.hypotheses]

    def suggest(self, n: int = 1) -> List[float]:
        """
        Suggest a promising point to probe next.

        Returns
        --------
        List[List[float]] : The suggested samples.
        """
        # If the space is empty, suggest a random point
        if len(self._space) == 0:
            suggestions = self._space.random_points(n=n)
            random_suggestions = [self._space.array_to_params(s) for s in suggestions]
            return random_suggestions

        # Finding argmax of the acquisition function.
        # Fit gp is set to False as it is already fitted in the
        # _get_mean_uncertainty
        suggestions = self._acquisition_function.suggest(
            gp=self._gp, target_space=self._space, fit_gp=False, n=n
        )

        # Check for duplicate points
        if not self._allow_duplicate_points:
            for i in range(len(suggestions)):
                s = suggestions[i]
                if s in self._space:
                    # Generate a random point
                    print("Duplicate point found. Generating a random point.")
                    s = self._space.random_points(n=1)[0]
                    suggestions[i] = s
                    self._hypothesis_names[i] = "None"
        return [self._space.array_to_params(s) for s in suggestions]

    def probe(self, params, lazy: bool = True):
        """Evaluate the function at the given points.

        Useful to guide the optimizer.

        Parameters
        ----------
        params: dict or list
            The parameters where the optimizer will evaluate the function.

        lazy: bool, optional(default=True)
            If True, the optimizer will evaluate the points when calling
            maximize(). Otherwise it will evaluate it at the moment.
        """
        if lazy:
            self._queue.add(params)
        else:
            self._space.probe(params)
            name = self._hypothesis_names.pop(0)
            self._space._hypothesis_tracking.append(name)

            # Log the optimization step
            self.dispatch(Events.OPTIMIZATION_STEP)

    def register(self, params, target, constraint_value=None):
        """Register an observation with known target.

        Parameters
        ----------
        params: dict or list
            The parameters associated with the observation.

        target: float
            Value of the target function at the observation.

        constraint_value: float or None
            Value of the constraint function at the observation, if any.
        """
        self._space.register(params, target, constraint_value)
        self.dispatch(Events.OPTIMIZATION_STEP)

    def maximize(
        self,
        n_init_points: int = 5,
        n_iter: int = 25,
    ):
        r"""
        Maximize the given function over the target space.

        Parameters
        ----------
        n_init_points : int, optional(default=5)
            Number of iterations before the explorations starts the exploration
            for the maximum.

        n_iter: int, optional(default=50)
            Number of iterations where the method attempts to find the maximum
            value.

        """
        # ----------------------- Initialize the optimizer --------------------
        self._prime_subscriptions()
        self.n_init_points = n_init_points
        self._initialize_queue(n_init_points)
        self.dispatch(Events.COMMENT_START)
        self._previous_best_value = -np.inf
        self.budget = n_init_points + n_iter
        iteration = 0

        # ----------------------- Start the optimization process --------------

        self.dispatch(Events.OPTIMIZATION_START)
        while not self._queue.empty or iteration < self.budget:
            x_probe_list = self._get_next_probe_list()

            # Evaluate the suggested points
            for x_probe in x_probe_list:
                self.probe(x_probe, lazy=False)
                iteration += 1

                # Stop the optimization if we have reached the budget
                if iteration == self.budget:
                    break

            # Update the policy after the initialization
            if iteration == self.n_init_points:
                mean_uncertainty = self._get_mean_uncertainty()
                self._policy.initialize(
                    iteration,
                    self.max["target"],
                    mean_uncertainty,
                )
            elif iteration > self.n_init_points:
                last_targets = self._space.target[-len(x_probe_list) :]
                mean_uncertainty = self._get_mean_uncertainty()
                self._policy.update(
                    last_targets,
                    self.max["target"],
                    iteration,
                    mean_uncertainty,
                )

            if self._bounds_transformer and iteration > self.n_init_points:
                # The bounds transformer should only modify the bounds after
                # the init_points points (only for the true iterations)
                self.set_bounds(self._bounds_transformer.transform(self._space))

        # ----------------------- End of the optimization ---------------------
        data_so_far = self._get_data_so_far()
        self.dispatch(Events.OPTIMIZATION_END)
        self._assistant.conclude(data_so_far)
        self.dispatch(Events.COMMENT_END)
        self._assistant.save_summary(self.max["target"])

    def save_data(self, folder_dir: str):
        """
        Save the optimization data to a file.

        Parameters
        ----------
        folder_dir : str
            The path where the data will be saved.
        """
        # Ensure the path exists
        os.makedirs(os.path.dirname(folder_dir), exist_ok=True)

        # Get the data
        data = self.res

        # Make sure bools are converted to strings
        if self.is_constrained:
            for d in data:
                d["allowed"] = str(d["allowed"])

        data = pd.DataFrame(data)

        # The "params" column is a dictionary, convert it to columns
        params = data["params"].apply(pd.Series)
        data = data.drop(["params"], axis=1)

        # Concatenate the params DataFrame and the data DataFrame along
        # the columns axis
        data = pd.concat([params, data], axis=1)

        # Change the index to be the iteration number and append 1 to the index
        data.index = data.index + 1
        data.index.name = "iteration"

        # Save the data as a csv file
        seed = self._assistant._random_seed
        path = os.path.join(
            folder_dir,
            f"data_{self._experiment.name}_d{self._experiment.dim}_s{seed}.csv",
        )
        data.to_csv(path)

        # Save the hypothesis records
        _json = json.dumps(self._hypothesis_records, indent=4)
        with open(path.replace(".csv", "_hypotheses.json"), "w") as f:
            f.write(_json)

        # Save the uncertainties
        uncertainties = self._policy._uncertainties
        uncertainties = pd.DataFrame(
            uncertainties, columns=["iteration", "uncertainty"]
        )
        uncertainties.to_csv(path.replace(".csv", "_uncertainties.csv"), index=False)

        # Save price
        price = self._assistant._get_price()
        price_file = path.replace(".csv", "_price.txt")
        with open(price_file, "w") as f:
            f.write(f"{price:.4f}$")
