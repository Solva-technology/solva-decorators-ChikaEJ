from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs_arg = ", ".join([f"{key} = {val}" for key, val in kwargs.items()])
        args_arg = ", ".join([f"{elem}" for elem in args])
        print(f"Вызов: {func.__name__}({args_arg or kwargs_arg})", end="\n")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper
