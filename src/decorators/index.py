from functools import wraps


def retry(attempts=1, exceptions=(), delay=1, backoff=1):
    def decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
                    current_delay *= backoff

        return wrapper

    return decorator
