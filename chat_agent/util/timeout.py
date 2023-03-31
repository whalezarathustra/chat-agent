import threading
from functools import wraps


class TimeoutError(Exception):
    pass


def timeout_decorator(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = [TimeoutError("Function timed out after {} seconds.".format(seconds))]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    result[0] = e

            t = threading.Thread(target=target)
            t.start()
            t.join(seconds)
            if isinstance(result[0], BaseException):
                raise result[0]
            return result[0]

        return wrapper

    return decorator
