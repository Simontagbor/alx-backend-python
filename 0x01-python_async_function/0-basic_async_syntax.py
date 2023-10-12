#!/usr/bin/env python3
"""
This module defines a simple function for testing asyncio module and random

Function:
- wait_random(max_delay: int,  default_value=10))
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine to introduce a random delay.

    Args:
        max_delay (int, optional): The maximum allowed delay in seconds.
            Defaults to 10.

    Returns:
        float: The randomly generated delay in seconds.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
