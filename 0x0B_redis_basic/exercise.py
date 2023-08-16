#!/usr/bin/env python3
'''Redis basic'''
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
import functools

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """Decorator which count how many times methods
    of the Cache class are called
    """
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper_count_calls(self, *args, **kwargs):
        """Inner Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_count_calls


def call_history(method: Callable) -> Callable:
    '''decorator to store the history of inputs and outputs
    for a particular function
    '''

    @functools.wraps(method)
    def wrapper_call_history(self, *args, **kwargs):
        """Inner Wrapper function"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output
    return wrapper_call_history


class Cache:
    ''' Cache redis class'''
    def __init__(self):
        ''' constructor for redis model'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        '''Store data into redis cache using a random key
        and returns the key'''
        random_key = str(uuid4())
        self._redis.mset({random_key: data})
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        '''Get the key from Redis'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''Parameterizes a value from redis to str'''
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        '''Parameterizes a value from redis to int'''
        value = self._redis.get(key)
        return int(value)
