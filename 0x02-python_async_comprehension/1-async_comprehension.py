#!/usr/bin/env python3
"""
module to practice asyncio

Function:
    async_comprehension: collects 10 async results.
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 Random numbers using an async comprehension

    Args:
        None:
    Returns:
        List of Random Numbers
    """
    results = [i async for i in async_generator()]
    return results
