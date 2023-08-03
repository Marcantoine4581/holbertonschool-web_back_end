#!/usr/bin/env python3
"""Let's duck type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length:
        Type-annotated function element_length.
    Args:
        lst (Iterable[Sequence[str]):
    Return:
        A list of tuple
    """
    return [(i, len(i)) for i in lst]
