
import redis


def create_redis_client():
    redis_host = 'localhost'
    redis_port = 6379
    return redis.Redis(host=redis_host, port=redis_port, db=0)
