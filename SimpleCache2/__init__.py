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
            _key = ""
            if key:
                _key = key
            else:
                _key = cache_system.getKey([args, kwargs], key_prefix)

            return cache_system.call(_key, ttl, original_function, *args, )

        return wrapper

    return decorating_function
