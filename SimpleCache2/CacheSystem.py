import pickle
from abc import ABC, abstractmethod
from typing import Callable

from SimpleCache2.utils import get_md5_hash


class CacheSystem(ABC):
    def __init__(self):
        self.clearOld()

    def getKey(self, key: any = None) -> str:
        """
        serialize key return key_prefix + md5(pickle.dumps(key))
        :param key:
        """
        return get_md5_hash(pickle.dumps(key))
        pass

    def call(self, key: any, ttl: int, callback: Callable, *args, **kwargs) -> any:
        """

        :param key:
        :param callback:
        :param ttl:
        """
        if self.exist(key):
            return self.get(key)
        else:
            value = callback(*args, **kwargs)
            self.set(key, value, ttl)
            return value
        pass

    @abstractmethod
    def exist(self, key: any) -> bool:
        """

        :param key:
        """
        pass

    @abstractmethod
    def get(self, key: any) -> any:
        """

        :param key:
        """
        pass

    @abstractmethod
    def set(self, key: any, value: object, ttl: int = 0):
        """

        :param key:
        :param value:
        :param ttl:
        """
        pass

    @abstractmethod
    def delete(self, key: any) -> bool:
        """

        :param key:
        """
        pass

    @abstractmethod
    def clearOld(self):
        pass

    pass
