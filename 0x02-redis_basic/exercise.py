#!/usr/bin/env python3
"""
Cache class to interact with Redis
"""
import redis
import uuid
from typing import Union, Callable

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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis based on the given key.

        Args:
            key (str): The key to retrieve the data.
            fn (Callable, optional): A callable function to apply to the retrieved data. Defaults to None.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data after applying the callable function, or None if the key doesn't exist.
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis as a string.

        Args:
            key (str): The key to retrieve the data.

        Returns:
            str: The retrieved data as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis as an integer.

        Args:
            key (str): The key to retrieve the data.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(key, int)
