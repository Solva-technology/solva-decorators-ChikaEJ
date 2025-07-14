from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key_of_cache = (args or tuple(kwargs.items()))

        if cache.get(key_of_cache) is None:
            cache[key_of_cache] = func(*args, **kwargs)
            return cache[key_of_cache]

        print("Из кэша")
        return cache[key_of_cache]

    return wrapper
