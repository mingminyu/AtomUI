from nicegui import app
from fastapi.responses import RedirectResponse
from functools import wraps


def is_auth(func):
    """验证用户登录是否合法，该验证比较简单，实际生产中需要替换更复杂的验证算法。"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not app.storage.user.get("authenticated", False):
            return RedirectResponse("/login")

        return func(*args, **kwargs)
    return wrapper
