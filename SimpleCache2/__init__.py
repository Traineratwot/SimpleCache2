from SimpleCache2.CacheSystem import CacheSystem


def simple_cache(cache_system: CacheSystem, ttl: int = 0, key_prefix: str = "", key: str = None):
    """
   Cache system decorator
    :param key_prefix:
    :param key:
    :param cache_system:
    :param ttl:
    :return:
    """

    def decorating_function(original_function):
        def wrapper(*args, **kwargs):
            if key:
                return cache_system.call(key, ttl, original_function, *args, )
            else:
                return cache_system.call([key_prefix, args, kwargs], ttl, original_function, *args, )

        return wrapper

    return decorating_function
