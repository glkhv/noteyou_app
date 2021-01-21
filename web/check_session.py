from pyramid.session import SignedCookieSessionFactory

from functools import wraps


def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'log_in' in request.session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
