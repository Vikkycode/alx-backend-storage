#!/usr/bin/env python3
"""
Cache class with replay function to
display call history
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
        """Wrapper function to log inputs and
        outputs."""
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

def replay(method: Callable):
    """Display the history of calls for a particular function."""
    # Get the Redis instance from the self object (the first argument of the method)
    redis_instance = method.__self__._redis
    
    # Get the method's qualified name
    method_name = method.__qualname__
    
    # Retrieve the inputs and outputs from Redis using LRANGE
    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)
    
    # Print the number of times the method was called
    print(f"{method_name} was called {len(inputs)} times:")
    
    # Iterate over inputs and outputs together using zip
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key and return the key."""
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store data in Redis
        return key  # Return the generated key

    def get(self, key: str) -> Union[str, None]:
        """Retrieve data from Redis by key."""
        return self._redis.get(key)

