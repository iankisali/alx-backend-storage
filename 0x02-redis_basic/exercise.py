#!/usr/bin/env python3
"""Redis Exercises combined"""
import sys
from typing import Union, Callable, Optional
from uuid import uuid4
import redis
UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """Writing strings to Redis"""
    def __init__(self):
        """ store an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """method should generate a random key (e.g. using uuid), store
        the input data in Redis using the random key and return the key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
