#!/usr/bin/env python3
""" type-annotated function sum_list"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function sum_list"""

    def multiplier_function(x: float) -> float:
        """ type-annotated function sum_list"""
        return x * multiplier

    return multiplier_function
