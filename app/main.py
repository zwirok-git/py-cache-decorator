from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in cache_dict.keys():
            print("Getting from cache")
            return cache_dict[args]

        else:
            cache_dict.update({args: func(*args, **kwargs)})
            print("Calculating new result")
            return cache_dict[args]

    return wrapper
