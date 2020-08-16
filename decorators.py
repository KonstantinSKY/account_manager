import sys
import functools
from typing import Callable, Any, Optional
from say import Say


def try_decor(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator for robust exception handling.
    Catches generic exceptions, logs the error with traceback info,
    and prevents application crash.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            error_msg = (
                f"CRITICAL ERROR in <{func.__name__}>\n"
                f"Type: {exc_type.__name__}\n"
                f"Message: {str(e)}\n"
                f"Args: {args}, Kwargs: {kwargs}"
            )
            Say(error_msg).prn_err()
            return None  # Explicitly return None on failure

    return wrapper
