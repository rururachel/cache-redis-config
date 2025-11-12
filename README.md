import redis
from typing import Any, Dict

class CacheManager:
    def __init__(self, host: str, port: int, db: int = 0):
        self.redis_client = redis.Redis(host=host, port=port, db=db)

    def set(self, key: str, value: Any, expire: int = 0):
        """Sets a cache item with the specified expiration time."""
        self.redis_client.set(key, value, expire)

    def get(self, key: str):
        """Retrieves a cache item."""
        return self.redis_client.get(key)

    def delete(self, key: str):
        """Deletes a cache item."""
        self.redis_client.delete(key)

    def get_all(self) -> Dict[str, Any]:
        """Retrieves all cache items."""
        return self.redis_client.keys()

    def clear(self):
        """Clears all cache items."""
        self.redis_client.flushdb()

    def expire(self, key: str, time: int):
        """Sets a cache item expiration time."""
        self.redis_client.expire(key, time)

    def ttl(self, key: str) -> int:
        """Returns the time to live for a cache item."""
        return self.redis_client.ttl(key)

def main():
    # Example usage
    cache_manager = CacheManager('localhost', 6379)
    cache_manager.set('key', 'value', 60)
    print(cache_manager.get('key'))
    cache_manager.delete('key')

if __name__ == '__main__':
    main()