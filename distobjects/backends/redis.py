import redis

class RedisBackend(object):
    def __init__(self, client:redis.Redis, prefix:str="" ):
        self.client = client
        self.prefix = prefix

    def get_redis_key(self, group:str) -> str:
        return self.prefix+group


    def fetch_value(self, group:str, key: str) -> str:
        return self.client.hget(self.get_redis_key(group), key)

    def save_value(self, group:str, key: str, value: str) -> None:
        self.client.hset(self.get_redis_key(group), key, value)

    def clear_value(self, group:str, key: str) -> None:
        self.client.hdel(self.get_redis_key(group), key)

    def fetch_group(self, group:str) -> dict:
        return self.client.hgetall(self.get_redis_key(group))

    def save_group(self, group:str, items:dict) -> None:
        with self.client.pipeline() as pipe:
            pipe.delete(self.get_redis_key(group))
            pipe.hmset(self.get_redis_key(group), items)
            pipe.execute()

    def clear_group(self, group:str) -> None:
        self.client.delete(self.get_redis_key(group))

