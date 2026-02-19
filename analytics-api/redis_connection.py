import redis 
import os

class RedisConn: 
    connection = None 
    host = os.getenv('REDIS_HOST', 'localhost')
    port = int(os.getenv('REDIS_PORT', 6379))

    @classmethod 
    def get_redis_connection(cls):
        if cls.connection is None:
            cls.connection = redis.Redis(host=cls.host, port=cls.port, decode_responses=True)
        return cls.connection


