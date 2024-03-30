#!/usr/bin/env python3

"""Page index module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a function that returns the start and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
