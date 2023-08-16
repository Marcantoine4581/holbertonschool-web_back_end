#!/usr/bin/env python3
'''Redis basic'''
import redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache:
    ''' Cache redis class'''
    def __init__(self):
        ''' constructor for redis model'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store data into redis cache'''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        '''Get the key from Redis'''
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        '''get a string from a byte string'''
        return string.decode("utf-8")

    def get_int(self, number: int) -> int:
        '''get an integer'''
        return int(number)
