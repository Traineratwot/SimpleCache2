import os.path
import pickle
from os import getenv
from os.path import expanduser, expandvars, dirname, realpath, getmtime, getctime, join
from time import time

from SimpleCache2.CacheSystem import CacheSystem


# os.path.getctime
# os.utime(file_path, (creation_time, modification_time))
class FileCache(CacheSystem):
    cache_dir: str

    def __init__(self, cache_dir: str = None):
        self.cache_dir = expanduser(expandvars(getenv('DISK_CACHE_DIR', os.path.join(dirname(realpath(__file__)), 'disk_cache'))))
        if cache_dir:
            self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)
        super().__init__()

    def exist(self, key: any) -> bool:
        path = self.getPath(key)
        return os.path.exists(path) and self.getEndTime(path) > time()
        pass

    def get(self, key: any) -> any:
        with open(self.getPath(key), "rb") as file:
            deserialized_data = pickle.load(file)
        return deserialized_data

    def set(self, key: any, value: object, ttl: int = 0) -> object:
        path = self.getPath(key)
        with open(path, "wb") as file:
            pickle.dump(value, file)
        os.utime(path, (time(), ttl))
        return self
        pass

    def delete(self, key: any) -> bool:
        path = self.getPath(key)
        os.unlink(path)
        return os.path.exists(path)
        pass

    def clearOld(self) -> list:
        file_list = []
        for root, dirs, files in os.walk(self.cache_dir):
            for file in files:
                now = time()
                path = os.path.join(root, file)
                end = self.getEndTime(path)
                if end and end < now:
                    os.unlink(path)
                    file_list.append(path)
        return file_list
        pass

    def pathJoin(self, *args):
        return "/".join(list(args))

    def getPath(self, key: any) -> str:
        _key = self.getKey(key)
        return join(self.cache_dir, _key)

    def getEndTime(self, path: str) -> float:
        create_time = getctime(path)
        ttl = self.getTTl(path)
        if ttl == 0:
            return 0
        return create_time + ttl

    def getTTl(self, path: str) -> float:
        return getmtime(path)
