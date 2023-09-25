import os.path
from time import time

from simple_cache.CacheSystem import CacheSystem


# os.path.getctime
# os.utime(file_path, (creation_time, modification_time))
class FileCache(CacheSystem):

    def __init__(self, cache_dir: str = None):
        self.cache_dir = os.path.join(os.getcwd(), "cache")
        if cache_dir:
            self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)
        super().__init__()

    def exist(self, key: any) -> bool:
        path = self.getPath(key)
        return os.path.exists(path) and os.path.getctime(path) < time()
        pass

    def get(self, key: any) -> any:
        pass

    def set(self, key: any, value: object, ttl: int = 0) -> object:
        pass

    def delete(self, key: any) -> object:
        pass

    def clearOld(self) -> object:
        pass

    def pathJoin(self, *args):
        return "/".join(list(args))

    def getPath(self, key: any) -> str:
        _key = self.getKey(key)
        return os.path.join(self.cache_dir, _key)
