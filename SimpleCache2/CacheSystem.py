import pickle
import re
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
        if self.is_valid_filename(key):
            return key
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

    def is_valid_filename(self, filename) -> bool:
        if not filename:
            return False
        # Проверяем, что строка не пустая
        if not isinstance(filename, str):
            return False

        # Проверяем, что строка не содержит запрещенных символов
        forbidden_chars = r'[<>:"/\\|?*\x00-\x1F]'
        if re.search(forbidden_chars, filename):
            return False

        # Проверяем, что строка не начинается с точки (скрытый файл)
        if filename.startswith('.'):
            return False

        # Проверяем, что строка не заканчивается точкой или пробелом
        if filename.endswith('.') or filename.endswith(' '):
            return False

        # Проверяем, что длина строки не превышает максимально допустимую
        max_length = 255
        if len(filename) > max_length:
            return False

        # Если все проверки пройдены, возвращаем True
        return True
