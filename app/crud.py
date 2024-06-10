from datetime import datetime
import json
import redis
from app.schemas import CryptoCreate, Crypto

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def create_crypto(data: CryptoCreate):
    timestamp = datetime.utcnow()
    crypto_data = Crypto(name=data.name, price=data.price, timestamp=timestamp)
    redis_key = f"crypto:{crypto_data.name}"
    redis_client.set(redis_key, crypto_data.json())
    return crypto_data


def get_crypto(name: str):
    redis_key = f"crypto:{name}"
    crypto_json = redis_client.get(redis_key)
    if crypto_json is None:
        return None
    crypto_data = json.loads(crypto_json)
    return Crypto(**crypto_data)


def get_all_cryptos():
    keys = redis_client.keys("crypto:*")
    cryptos = []
    for key in keys:
        crypto_json = redis_client.get(key)
        crypto_data = json.loads(crypto_json)
        cryptos.append(Crypto(**crypto_data))
    return cryptos


def update_crypto(name: str, data: CryptoCreate):
    redis_key = f"crypto:{name}"
    if not redis_client.exists(redis_key):
        return None
    timestamp = datetime.utcnow()
    crypto_data = Crypto(name=data.name, price=data.price, timestamp=timestamp)
    redis_client.set(redis_key, crypto_data.json())
    return crypto_data


def delete_crypto(name: str):
    redis_key = f"crypto:{name}"
    if not redis_client.exists(redis_key):
        return False
    redis_client.delete(redis_key)
    return True
