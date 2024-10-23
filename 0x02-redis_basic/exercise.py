#!/usr/bin/env python3
"""
Cache class to interact with Redis
"""
import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class to interact with Redis
    """
    def __init__(self):
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key and return the key"""
        key = str(uuid.uuid4())  # Generate a random key using uuid4
        self._redis.set(key, data)  # Store data in Redis
        return key  # Return the random key

