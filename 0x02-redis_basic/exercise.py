#!/usr/bin/env python3
"""
Cache class with count_calls decorator
to count method calls
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a
    method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments
        the call count in Redis."""

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and
        flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random
        key and return the key."""
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis
        return key  # Return the generated key

    def get(self, key: str) -> Union[str, None]:
        """Retrieve data from Redis by key."""
        return self._redis.get(key)
