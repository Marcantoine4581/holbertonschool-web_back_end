#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n:
        asynchronous coroutine.
    Args:
        n (int) : integer
        max_delay (int) : integer
    Return:
        A list of floats numbers in ascending order.
    """
    results: List[float] = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    return [await result for result in asyncio.as_completed(results)]
