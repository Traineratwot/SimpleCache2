import pickle

from SimpleCache2.CacheSystem import CacheSystem


class LruCache(CacheSystem):
    memory: {}

    def __init__(self):
        self.memory = {}
        super().__init__()

    def exist(self, key: any) -> bool:
        k = self.getKey(key)
        return k in self.memory

    def get(self, key: any) -> any:
        k = self.getKey(key)
        if k in self.memory:
            return pickle.loads(self.memory[k])
        return None

    def set(self, key: any, value: object, ttl: int = 0) -> object:
        k = self.getKey(key)
        self.memory[k] = pickle.dumps(value)
        return self

    def delete(self, key: any) -> bool:
        self.memory[self.getKey(key)] = None
        return True

    def clearOld(self) -> list:
        self.memory = {}
