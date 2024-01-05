#!/usr/bin/env python3
""" type-annotated function sum_list"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ type-annotated function sum_list"""
    return (k, v**2)
