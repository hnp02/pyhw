import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "")
        return result
    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def all_true(*args):
    return True


@logger_decorator
def describe(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    all_true(1, 2, 3)
    describe(name="Ann", age=30)
