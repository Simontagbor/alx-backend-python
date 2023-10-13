#!/usr/bin/env python3
"""
module to practice asyncio

Function:
    measure_runtime(): Measures the runtime performance
    of calling a coroutine four times
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures runtime of calling asyncio_comprehension 4 times

    Args:
        None
    Returns:
        time (float): seconds it took to run
        four parallel asyncio comps
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension())
    end = time.perf_counter()
    elapsed = end - start
    return elapsed
