import functools

from testnet_setup import DEBUG

LOGGING_BOOL = DEBUG


def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except AttributeError as e:
            if LOGGING_BOOL:
                print(e)
            return 'KEY/SECRET not valid or not existing'
    return wrapper
