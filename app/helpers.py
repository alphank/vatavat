from flask import session, redirect
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None or User.Role.ADMIN.value not in session.get("role"):
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function