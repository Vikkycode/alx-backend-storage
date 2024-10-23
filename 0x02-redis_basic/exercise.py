#!/usr/bin/env python3
""" Cache class """
import redis
import uuid


class Cache:
    """
    Cache class using Redis
    """
    def __init__(self):
        """
        Initialize Redis client and flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
       Store data in Redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
