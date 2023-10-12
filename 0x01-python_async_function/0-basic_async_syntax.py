#!/usr/bin/env python3

import asyncio
import random


"""
This module defines a simple function for testing asyncio module and random
Usage: asyncio.run(wait_random(max_delay: int | default_value=10))
"""


async def wait_random(max_delay: int = 10) -> float:

    """waits for a random amount of seconds and
    returns the float value of the wait time

    Args: max_delay(int) the maximum delay limit
    Returns: random_delay(float)
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
