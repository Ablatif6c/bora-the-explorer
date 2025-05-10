"""Register optimization events variables."""


class Events:
    """Define optimization events.

    Behaves similar to enums.
    """
    OPTIMIZATION_START = "optimization:start"
    OPTIMIZATION_STEP = "optimization:step"
    OPTIMIZATION_END = "optimization:end"
    COMMENT_START = "comment:start"
    COMMENT_STEP = "comment:step"
    COMMENT_END = "comment:end"


DEFAULT_EVENTS = [
    Events.OPTIMIZATION_START, Events.OPTIMIZATION_STEP,
    Events.OPTIMIZATION_END, Events.COMMENT_START, Events.COMMENT_STEP,
    Events.COMMENT_END
]
