#!/usr/bin/env python3
"""This module define a function index_range
This function takes page number and page size and then return tuple of the
corresponding page ranges
"""


def index_range(page, page_size):
    """Get the start_index and end_index of page size and number
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
