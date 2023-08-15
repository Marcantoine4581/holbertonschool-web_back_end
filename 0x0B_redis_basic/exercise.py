#!/usr/bin/env python3
'''Redis basic'''
import redis
from typing import Union
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
