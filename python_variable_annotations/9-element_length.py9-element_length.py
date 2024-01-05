#!/usr/bin/env python3
""" type-annotated function sum_list"""
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ type-annotated function sum_list"""
    lst = []

    for i in lst:
        lst.append(i, len(i))
    return lst
