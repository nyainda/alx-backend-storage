#!/usr/bin/env python3
""" Web """

import requests
import redis
from Typing import Callable
from functools import wraps


_redis = redis.Redis()


def count_url_wrapper(method: Callable) -> Callable:
    """ Decorator counting how many times
    a Url is accessed """
    @wraps(method)
    def wrapper(url):
        hashed_url = f'hashed_url:{url}'
        hashed_counter = f'count:{url}'

        response_html = method(url)

        _redis.incr(hashed_counter)
        _redis.set(hashed_url, response_html)
        _redis.expire(hashed_url, 10)
        return response_html if not _redis.get(hashed_url) else _redis.get(
            hashed_url)
    return wrapper


@count_url_wrapper
def get_page(url: str) -> str:
    """ Get page """
    return requests.get(url).text
