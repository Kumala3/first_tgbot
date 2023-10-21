def allow_access(is_allowed=None):
    def decorator(func):
        setattr(func, 'allow', is_allowed)
        return func

    return decorator
