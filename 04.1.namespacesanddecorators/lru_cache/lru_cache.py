import functools
from collections import OrderedDict
from typing import Callable, Any, TypeVar

Function = TypeVar('Function', bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Function], Function]:
    """
    Returns decorator, which stores result of function
    for `max_size` most recent function arguments.
    :param max_size: max amount of unique arguments to store values for
    :return: decorator, which wraps any function passed
    """

    def lru_cache(func):  # type: ignore
        lru_cache.cash = OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # type: ignore
            if (*args, tuple(set(**kwargs))) in lru_cache.cash.keys():
                return lru_cache.cash[(*args, tuple(set(**kwargs)))]
            else:
                result = func(*args, **kwargs)
                if len(lru_cache.cash) >= max_size:
                    lru_cache.cash.popitem(False)
                lru_cache.cash.setdefault((*args, tuple(set(**kwargs))), result)
            return result

        return wrapper

    return lru_cache
