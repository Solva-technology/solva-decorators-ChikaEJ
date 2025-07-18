from functools import wraps


def validate_positive(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if min(args or kwargs.values()) < 0:
            raise ValueError("Все аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper
