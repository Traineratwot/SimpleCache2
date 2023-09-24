def simple_cache(ttl: int = 0, keyPrefix: str = None, cacheDir: str = None, key: str = None):
    """
   Cache system decorator
    :param ttl:
    :return:
    """

    def decorating_function(original_function):
        def wrapper(*args, **kwargs):
            function_value = original_function(*args, **kwargs)
            return function_value

        return wrapper

    return decorating_function
