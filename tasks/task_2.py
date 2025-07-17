from functools import wraps

NO_ARGS_KWARGS = 0
NO_ARGS_KWARGS_STR = "No arguments"


def check_args(args, kwargs):

    if len(args) > NO_ARGS_KWARGS:
        return str(args)
    elif len(kwargs) > NO_ARGS_KWARGS:
        return str(sorted(kwargs))

    return NO_ARGS_KWARGS_STR


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key_of_cache = check_args(args, kwargs)

        if cache.get(key_of_cache) is None:
            cache[key_of_cache] = func(*args, **kwargs)
            return cache[key_of_cache]

        print("Из кэша")
        return cache[key_of_cache]

    return wrapper
