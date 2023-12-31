#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    Args:
        page (int): the number of the page.
        page_size (int): the size of each page.
    Returns:
        A tuple of size two containing a start index and an end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return(start, end)
