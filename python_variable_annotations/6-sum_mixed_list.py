#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_list:
        Type-annotated function sum_list which takes a list input_list
        of floats as argument and returns their sum as a float.
    Args:
        input_list (list[float]) : list of float number
    Return:
        A float number.
    """
    result: float = 0
    for num in mxd_lst:
        result += num
    return result
