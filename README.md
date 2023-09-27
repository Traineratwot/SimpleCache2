# SimpleCache

## Usage

```python
from SimpleCache2 import simple_cache
from SimpleCache2.FileCache import FileCache
from SimpleCache2.MemoryCache import MemoryCache
from SimpleCache2.Settings import Settings

# save cache in python variable 
memory = MemoryCache()
# save cache in one json file 
settings = Settings(settings_file="path/to/test.json")
# save cache in many binary files
cache = FileCache(cache_dir=None)


# Usage as decorator
@simple_cache(cache, ttl=10, key_prefix="test_")
def testFunc(name):
    return f"hello world {name}"


# Usage as callback
cache.call(["cache key can be any value"], 10, testFunc, "Bob")

# Usage as functional
cache.set("key", "value")  # self
cache.get("key")  # value
cache.exist("key")  # bool
cache.delete("key")  # bool
cache.clearOld()  # bool
```

## Api

You can write you self cache class:

```python
from SimpleCache2.CacheSystem import CacheSystem


class MyCacheClass(CacheSystem):
    def exist(self, key: any) -> bool:
        pass

    def get(self, key: any) -> any:
        pass

    def set(self, key: any, value: object, ttl: int = 0) -> object:
        return self
        pass

    def delete(self, key: any) -> bool:
        pass

    def clearOld(self):
        pass
```