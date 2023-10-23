#!/usr/bin/env python3
"""a function named index_range that takes\
   two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page <= 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
