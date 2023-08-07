#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time:
        Function that measures the total execution time for
        wait_n(n, max_delay).
    Args:
        n (int) : integer
        max_delay (int) : integer
    Return:
        A float numbers equal to (total_time / n).
    """
    start = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    end = time.process_time()
    return (end - start) / n
