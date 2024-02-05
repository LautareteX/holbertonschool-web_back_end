#!/usr/bin/env python3
"""
collect random numbers using an async comprehensing
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    collect random numbers using an async comprehensing
    """
    return [item async for item in async_generator()]
