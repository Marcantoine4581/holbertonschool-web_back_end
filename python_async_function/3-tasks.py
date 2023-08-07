#!/usr/bin/env python3
"""Asyncio Task"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    measure_time:
        Function.
    Args:
        max_delay (int) : integer
    Return:
        A asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
