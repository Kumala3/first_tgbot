def rate_limit(limit: int, key=None, num_messages=None):
    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "throttling_key", key)
        if num_messages:
            setattr(func, "throttling_num_messages", num_messages)
        return func

    return decorator
