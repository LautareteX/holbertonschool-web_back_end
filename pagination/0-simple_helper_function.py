#!/usr/bin/env python3
"""function that takes two integer arguments"""


def index_range(page, page_size) -> tuple:
    """function that takes two integer arguments"""
    return (page * page_size) - page_size, page * page_size
