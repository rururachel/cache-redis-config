import logging
from typing import Dict, List

class ConfigLoader:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        try:
            with open(self.config_file, 'r') as file:
                config = {}
                for line in file:
                    key, value = line.strip().split('=')
                    config[key.strip()] = value.strip()
                return config
        except FileNotFoundError:
            logging.error(f"Config file {self.config_file} not found.")
            return {}

    def get_config(self) -> Dict:
        return self.config

class CacheConfig:
    def __init__(self, host: str, port: int, db: int):
        self.host = host
        self.port = port
        self.db = db

class RedisConfig:
    def __init__(self, host: str, port: int, db: int):
        self.host = host
        self.port = port
        self.db = db

def get_config(config_file: str) -> Dict:
    loader = ConfigLoader(config_file)
    config = loader.get_config()
    return config

def get_cache_config(config: Dict) -> CacheConfig:
    host = config.get('cache_host', 'localhost')
    port = config.get('cache_port', 6379)
    db = config.get('cache_db', 0)
    return CacheConfig(host, port, db)

def get_redis_config(config: Dict) -> RedisConfig:
    host = config.get('redis_host', 'localhost')
    port = config.get('redis_port', 6379)
    db = config.get('redis_db', 0)
    return RedisConfig(host, port, db)