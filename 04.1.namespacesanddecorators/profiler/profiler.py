import datetime
import functools
from typing import Any


def profiler(func):  # type: ignore
    """
    Returns profiling decorator, which counts calls of function
    and measure last function execution time.
    Results are stored as function attributes: `calls`, `last_time_taken`
    :param func: function to decorate
    :return: decorator, which wraps any function passed
    """
    profiler.calls = 0
    profiler.last_time_taken = datetime.datetime.now()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # type: ignore
        initial_calls = profiler.calls
        profiler.calls += 1
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        wrapper.last_time_taken = (datetime.datetime.now() - start_time).total_seconds()
        wrapper.calls = profiler.calls - initial_calls
        return result
    return wrapper
