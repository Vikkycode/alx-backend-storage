#!/usr/bin/env python3
"""
Cache class with call_history
decorator to store input/output history
"""
import redis
import uuid
from typing import Callable, Union
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs
    and outputs in Redis."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to log inputs
        and outputs."""
        # Create Redis keys for inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Store the input arguments (ignore kwargs for now)
        self._redis.rpush(input_key, str(args))

        # Call the original method and get the result
        result = method(self, *args, **kwargs)

        # Store the result/output
        self._redis.rpush(output_key, str(result))

        # Return the result of the original method
        return result

    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key and
        return the key."""
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis
        return key  # Return the generated key

    def get(self, key: str) -> Union[str, None]:
        """Retrieve data from Redis by key."""
        return self._redis.get(key)
