#!/usr/bin/env python3
"""Basic annotations - concat funtion"""


def concat(str1: str, str2: str) -> str:
    """
    concat:
        Type-annotated function concat that takes a string str1 and
        a string str2 as arguments and returns a concatenated string.
    Args:
        str1 (str) : string to concat
        str2 (str) : string to concat
    Return:
        A concatenated string
    """
    return "{}{}".format(str1, str2)
