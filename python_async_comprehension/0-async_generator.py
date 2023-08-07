#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator:
        Coroutine called async_generator that takes no arguments.
    Args:
        Nothing.
    Return:
        A random number between 0 and 10.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
