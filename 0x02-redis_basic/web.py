#!/usr/bin/env python3
"""
Web cache and URL tracker using Redis
"""
import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
r = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL
    and cache it in Redis for 10 seconds.
    Track the number of times the URL
    was accessed.
    """
    # Check if the URL content is cached in Redis
    cached_content = r.get(f"cached:{url}")
    if cached_content:
        return cached_content.decode("utf-8")

    # If not cached, fetch the content using requests
    response = requests.get(url)
    content = response.text

    # Cache the fetched content in Redis with a 10-second expiration
    r.setex(f"cached:{url}", 10, content)

    # Increment the counter to track how many times the URL was accessed
    r.incr(f"count:{url}")

    return content


def display_url_access_count(url: str) -> int:
    """
    Display how many times a URL was accessed.
    """
    count = r.get(f"count:{url}")
    return int(count) if count else 0
