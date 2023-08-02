#!/usr/bin/env python3
"""Basic annotations - add funtion"""


def add(a: float, b: float) -> float:
    """
    add:
        Type-annotated function that takes a float a and a float b as
        arguments and returns their sum as a float.
    Args:
        a (float) : float number
        b (float) : float number
    Return:
        sum of a and b as a float
    """
    return a + b
