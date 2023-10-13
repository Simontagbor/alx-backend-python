#!/usr/bin/env python3
"""
module to practice asyncio

Function:
    async_generator(): loops 10 times yielding 10 random floats.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops Ten times with 10 yields of random floats.

    Args:
        None:

    Yields:
        float: Random floats
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
