from src.infra.cache.icache import ICacheCliente
import redis
import os
from src.utils import logger


class RedisClient(ICacheCliente):
    def __init__(self):
        try:
            self.redis_client = redis.StrictRedis.from_url(
                os.environ.get("REDIS_URL"))
        except Exception as ex:
            logger.critical(f"Error connecting to Redis - {ex}")
            None

    def create(self, key, value, ttl=None):
        """Cria uma entrada no Redis."""
        try:
            self.redis_client.set(key, value, ex=ttl)
            return True
        except:
            return

    def get(self, key):
        """Obtém um valor do Redis com base na chave."""
        return self.redis_client.get(key)

    def remove(self, key):
        """Remove uma entrada do Redis com base na chave."""
        self.redis_client.delete(key)
