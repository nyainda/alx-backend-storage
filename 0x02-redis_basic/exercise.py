#!/usr/bin/env python3
""" Exercise """


import uuid
import redis
from typing import Union, Optional, Callable
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Implementing counter """
    key_counter = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ incr count """
        self._redis.incr(key_counter)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Implementing history """
    inputs = f'{method.__qualname__}:inputs'
    outputs = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ append to history """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(fn):
    """ calls history """
    store = redis.Redis()
    input_key = f"{fn.__qualname__}:inputs"
    output_key = f"{fn.__qualname__}:outputs"
    count = store.get(fn.__qualname__).decode("utf-8")
    print(f"{fn.__qualname__} was called {count} times:")

    inputs = store.lrange(input_key, 0, count)
    outputs = store.lrange(output_key, 0, count)

    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print("{}(*{}) -> {}".format(fn.__qualname__, input, output))


class Cache():
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        Get data from cache or call function
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, value: bytes) -> str:
        """
        Get data from cache as string
        """
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
        """
        Get data from cache as int
        """
        return int.from_bytes(value, sys.byteorder)
