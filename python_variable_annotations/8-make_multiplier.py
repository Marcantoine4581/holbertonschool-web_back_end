#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier:
        Type-annotated function make_multiplier that takes a float multiplier
        as argument and returns a function that multiplies a float
        by multiplier.
    Args:
        multiplier (float): A float number
    Return:
        A function that multiplies a float by multiplier.
    """
    def multi(num: float) -> float:
        """multi: function that multiplies num by multiplier"""
        return num * multiplier

    return multi
