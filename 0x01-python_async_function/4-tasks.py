#!/usr/bin/env python3
"""
This module contains functions for testing Asyncio using the ayncio module

Functions:
    - task_wait_n(n, max_delay) returns a list of all delays.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a List of Delays


    Args:
        n (int): number of times to run function
        max_delay (int): the maximum delay value

    Returns:
        list: the list of delay values
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)

    return sorted(results)
