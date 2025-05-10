"""Contains classes and functions for logging."""

from __future__ import print_function

import json
import os

from colorama import Fore, just_fix_windows_console

from bora.experiment import Type

from .event import Events
from .observer import _Tracker

just_fix_windows_console()


def _get_default_logger(verbose, is_constrained, path, default_precision=4):
    """
    Return the default logger.

    Parameters
    ----------
    verbose : bool, optional(default=True)
        Verbosity level of the logger.

    is_constrained : bool
        Whether the underlying optimizer uses constraints (this requires
        an additional column in the output).

    Returns
    -------
    ScreenLogger
        The default logger.

    """
    ScreenLogger._default_precision = default_precision + 1
    return ScreenLogger(
        verbose=verbose,
        is_constrained=is_constrained,
        path=path,
    )


class ScreenLogger(_Tracker):
    """Logger that outputs text, e.g. to log to a terminal.

    Parameters
    ----------
    verbose : bool, optional(default=True)
        Whether to activate the verbosity level of the logger.

    is_constrained : bool
        Whether the logger is associated with a constrained optimization
        instance.
    """

    _default_cell_size = 9
    _default_precision = 4

    def __init__(self,
                 verbose: bool = True,
                 is_constrained=False,
                 path: str = None):
        self._verbose = verbose
        self._is_constrained = is_constrained
        self._header_length = None
        self.path = path  # Path to the file to write the logs to
        if self.path:
            try:
                os.makedirs(os.path.dirname(self.path))
            except FileExistsError:
                pass
            with open(self.path, "w") as f:
                f.write("")

        super().__init__()

    # @property
    # def verbose(self):
    #     """Return the verbosity level."""
    #     return self._verbose

    # @verbose.setter
    # def verbose(self, v):
    #     """Set the verbosity level.

    #     Parameters
    #     ----------
    #     v : int
    #         New verbosity level of the logger.
    #     """
    #     self._verbose = v

    @property
    def is_constrained(self):
        """Return whether the logger is constrained."""
        return self._is_constrained

    def _format_number(self, x):
        """Format a number.

        Parameters
        ----------
        x : number
            Value to format.

        Returns
        -------
        A stringified, formatted version of `x`.
        """
        if isinstance(x, float):
            s = f"{x:<{self._default_cell_size}.{self._default_precision}}"
        else:
            s = f"{x:<{self._default_cell_size}}"

        if len(s) > self._default_cell_size:
            if "." in s:
                return s[:self._default_cell_size]
            return s[:self._default_cell_size - 3] + "..."
        return s

    def _format_bool(self, x):
        """Format a boolean.

        Parameters
        ----------
        x : boolean
            Value to format.

        Returns
        -------
        A stringified, formatted version of `x`.
        """
        if 5 > self._default_cell_size:
            if x:
                x_ = "T"
            else:
                x_ = "F"
        else:
            x_ = str(x)
        s = f"{x_:<{self._default_cell_size}}"
        return s

    def _format_key(self, key):
        """Format a key.

        Parameters
        ----------
        key : string
            Value to format.

        Returns
        -------
        A stringified, formatted version of `x`.
        """
        s = f"{key:^{self._default_cell_size}}"
        if len(s) > self._default_cell_size:
            return s[:self._default_cell_size - 3] + "..."
        return s

    def _step(self, instance, colour=Fore.BLACK):
        """Log a step.

        Parameters
        ----------
        instance : bayesian_optimization.BayesianOptimization
            The instance associated with the event.

        colour :
            (Default value = Fore.BLACK)

        Returns
        -------
        A stringified, formatted version of the most recent optimization step.
        """
        res = instance.res[-1]
        cells = []

        cells.append(self._format_number(self._iterations + 1))
        cells.append(self._format_number(res["target"]))
        if self._is_constrained:
            cells.append(self._format_bool(res["allowed"]))

        for key in instance.space.keys:
            if instance._experiment.type is Type.categorical:
                parameter = instance._experiment.get_parameter(key)
                cells.append(
                    self._format_number(
                        str(parameter.categories[res["params"][key]])))
            else:
                cells.append(self._format_number(res["params"][key]))

        cells.append(res["hypotheses"])
        return "| " + " | ".join(
            [colour + cells[i] for i in range(len(cells))]) + " |"

    def _header(self, instance):
        """Print the header of the log.

        Parameters
        ----------
        instance : bayesian_optimization.BayesianOptimization
            The instance associated with the header.

        Returns
        -------
        A stringified, formatted version of the most header.
        """
        cells = []
        cells.append(self._format_key("iter"))
        cells.append(self._format_key("target"))

        if self._is_constrained:
            cells.append(self._format_key("allowed"))

        for key in instance.space.keys:
            cells.append(self._format_key(key))

        cells.append(self._format_key("hypotheses"))
        line = "| " + " | ".join(cells) + " |"
        self._header_length = len(line)
        return line + "\n" + ("-" * self._header_length)

    def _is_new_max(self, instance):
        """Check if the step to log produced a new maximum.

        Parameters
        ----------
        instance : bayesian_optimization.BayesianOptimization
            The instance associated with the step.

        Returns
        -------
        boolean
        """
        if instance.max is None:
            # During constrained optimization, there might not be a maximum
            # value since the optimizer might've not encountered any points
            # that fulfill the constraints.
            return False
        if self._previous_max is None:
            self._previous_max = instance.max["target"]
        return instance.max["target"] > self._previous_max

    def update(self, event, instance, *args, **kwargs):
        """Handle incoming events.

        Parameters
        ----------
        event : str
            One of the values associated with `Events.OPTIMIZATION_START`,
            `Events.OPTIMIZATION_STEP` or `Events.OPTIMIZATION_END`.

        instance : bayesian_optimization.BayesianOptimization
            The instance associated with the step.
        """
        if event == Events.OPTIMIZATION_START:
            line = self._header(instance) + "\n"
        elif event == Events.OPTIMIZATION_STEP:
            is_new_max = self._is_new_max(instance)
            if not self._verbose and not is_new_max:
                line = ""
            else:
                colour = Fore.MAGENTA if is_new_max else Fore.BLACK
                line = self._step(instance, colour=colour) + "\n"
        elif event == Events.OPTIMIZATION_END:
            line = "=" * self._header_length + "\n"
        elif event == Events.COMMENT_START:
            colour = Fore.BLACK
            comment = instance._assistant.last_comment
            line = (colour + instance._assistant.experiment_overview + "\n\n" +
                    str(comment) + "\n\n")
        elif event == Events.COMMENT_STEP:
            comment = instance._assistant.last_comment
            colour = Fore.BLACK
            line = colour + str(comment) + "\n\n"
        elif event == Events.COMMENT_END:
            colour = Fore.GREEN
            comment = instance._assistant.last_comment
            line = colour + comment.comment + "\n" + Fore.BLACK

        if self._verbose:
            print(line, end="")

            # Save the logs to a file
            if self.path:
                with open(self.path, "a") as f:
                    f.write(line)

        self._update_tracker(event, instance)


class JSONLogger(_Tracker):
    """
    Logger that outputs steps in JSON format.

    The resulting file can be used to restart the optimization from an earlier
    state.

    Parameters
    ----------
    path : str or bytes or os.PathLike
        Path to the file to write to.

    reset : bool
        Whether to overwrite the file if it already exists.

    """

    def __init__(self, path, reset=True):
        self._path = path
        if reset:
            try:
                os.remove(self._path)
            except OSError:
                pass
        super().__init__()

    def update(self, event, instance):
        """
        Handle incoming events.

        Parameters
        ----------
        event : str
            One of the values associated with `Events.OPTIMIZATION_START`,
            `Events.OPTIMIZATION_STEP` or `Events.OPTIMIZATION_END`.

        instance : bayesian_optimization.BayesianOptimization
            The instance associated with the step.

        """
        if event == Events.OPTIMIZATION_STEP:
            data = dict(instance.res[-1])

            now, time_elapsed, time_delta = self._time_metrics()
            data["datetime"] = {
                "datetime": now,
                "elapsed": time_elapsed,
                "delta": time_delta,
            }

            if "allowed" in data:
                # fix: github.com/fmfn/BayesianOptimization/issues/361
                data["allowed"] = bool(data["allowed"])

            with open(self._path, "a") as f:
                f.write(json.dumps(data) + "\n")

        self._update_tracker(event, instance)
