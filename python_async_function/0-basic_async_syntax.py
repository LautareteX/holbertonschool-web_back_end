#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument"""
    delay = random.uniform(0, max_delay) #Selecciona un numero random unfirom(flotante) entre 0 y max delay 
    await asyncio.sleep(delay) #Espera los segundos 
    return delay #Retorna los segundos
