#!/usr/bin/env python3
"""
This module contains functions for testing Asyncio using the ayncio module

Functions:
    - wait_n(n, max_delay) returns a list of all delays.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Returns a List of Delays


    Args:
        n (int): number of times to run function
        max_delay (int): the maximum delay value

    Returns:
        list: the list of delay values
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)

    return sorted(results)
