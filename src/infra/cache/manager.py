import json
import logging
import importlib
import inspect
import os
from src.utils import logger
from src.infra.cache import icache


class CacheManager:
    def __init__(self):
        self.instance = self.__load_instance(
            os.environ.get("CACHE_TYPE", "redis"))
        logging.info("cache connected!")

    def __load_instance(self, cache_name) -> icache.ICacheCliente:
        module = importlib.import_module(f"src.infra.cache.{cache_name}")
        classes = inspect.getmembers(module, inspect.isclass)
        found_manager = list(
            filter(lambda x: cache_name.capitalize() in x[0], classes))
        if not found_manager:
            raise Exception("Cache not found")
        return found_manager[0][1]()

    def __parse_dict(self, data: dict):
        """Convert json in string"""
        return json.dumps(data)

    def __decode_dict(self, data: str):
        """Convert string in json"""
        try:
            return json.loads(data)
        except:
            return data

    def save(self, key, data, ttl=None):
        """Save document in cache."""
        try:
            if type(data) is dict:
                data = self.__parse_dict(data)
            return self.instance.create(key, data, ttl)
        except Exception as e:
            logger.critical(
                {"message": "error saving cache",
                    "error": str(e), "payload": data}
            )

    def get(self, key):
        """Get document by key."""
        try:
            value = self.instance.get(key)
            if not value:
                return
            return self.__decode_dict(value)
        except:
            return

    def delete(self, key):
        """Delete document by key."""
        try:
            return self.instance.remove(key)
        except:
            return
