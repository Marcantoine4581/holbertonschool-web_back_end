#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv:
        Type-annotated function to_kv that takes a string k and an int OR
        float v as arguments and returns a tuple.
    Args:
        k (str): a string
        v (Union[int, float]) : An interger or a float number
    Return:
        A tuple with a string and a float number.
    """
    vSquare = (v * v)
    result: Tuple[str, float] = (k, vSquare)
    return result
