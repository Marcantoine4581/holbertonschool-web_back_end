#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension:
        Coroutine called async_comprehension that takes no arguments.
        The coroutine will collect 10 random numbers using an async
        comprehensing over async_generator.
    Args:
        Nothing.
    Return:
        The 10 random numbers.
    """
    return [i async for i in async_generator()]
