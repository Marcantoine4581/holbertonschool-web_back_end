#!/usr/bin/env python3
'''Redis basic'''
import redis
from typing import Union, Optional, Callable
from uuid import uuid4

UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    ''' Cache redis class'''
    def __init__(self):
        ''' constructor for redis model'''
        self._redis = redis.Redis()
        self._redis.flushdb()

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
