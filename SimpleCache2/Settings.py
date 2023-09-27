import json
import os.path
from os import makedirs, getenv
from os.path import dirname, exists, realpath, expanduser, expandvars
from io import open

from SimpleCache2.CacheSystem import CacheSystem


class Settings(CacheSystem):
    settings_file: str

    def __init__(self, settings_file: str = None):
        self.settings_file = expanduser(expandvars(getenv('DISK_CACHE_DIR', os.path.join(dirname(realpath(__file__)), 'disk_cache', "settings.json"))))
        self.settingsData = {}
        if settings_file:
            self.settings_file = settings_file
        makedirs(dirname(self.settings_file), exist_ok=True)
        super().__init__()
        self.load()

    def __del__(self):
        try:
            self.save()
        except ValueError:
            pass
        pass

    def __set__(self, instance, value):
        self.set(instance, value)

    def __delete___(self, instance):
        self.delete(instance)

    def __len__(self):
        return len(self.settingsData)

    def exist(self, key: any) -> bool:
        k = self.getKey(key)
        return k in self.settingsData
        pass

    def get(self, key: any) -> any:
        k = self.getKey(key)
        if k in self.settingsData:
            return self.settingsData[k]
        return None
        pass

    def set(self, key: any, value: object, ttl: int = 0) -> object:
        k = self.getKey(key)
        self.settingsData[k] = value
        self.save()
        return self
        pass

    def delete(self, key: any) -> bool:
        return False
        pass

    def clearOld(self) -> list:
        return []
        pass

    def load(self):
        if not exists(self.settings_file):
            self.save()
            return
        with open(self.settings_file, "rb") as file:
            self.settingsData = json.load(file)
        pass

    def save(self):
        with open(self.settings_file, "w") as file:
            json.dump(self.settingsData, file)
        pass
