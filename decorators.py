import sys


def try_decor(func):            # Decorator for handling exceptions
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("ERROR!!! - Cant execute function:", func)
            print(repr(e))
            print("Error:", sys.exc_info()[0])

    return inner
