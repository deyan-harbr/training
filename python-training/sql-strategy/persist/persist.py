from functools import wraps
from base import session_scope


def persist(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with session_scope() as session:
            session.add_all(func(*args, **kwargs))
    return wrapper
