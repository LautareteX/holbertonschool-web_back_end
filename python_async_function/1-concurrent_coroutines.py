#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """asynchronous coroutine that takes in an integer argument"""
    completed_tasks = []

    for _ in range(n):
        completed_tasks.append(await wait_random(max_delay))

    return sorted(completed_tasks)
