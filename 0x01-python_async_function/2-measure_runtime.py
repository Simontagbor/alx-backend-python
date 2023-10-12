#!/usr/bin/env python3
"""
This 2-measure_runtime module measures the
performance of the concurrent routines

Function:
    measure_time(n: int, max_delay: int)
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for a coroutine.

    Args:
        n (int): the number of time to execute the couroutine
        max_delay (int): the number of seconds to delay by

    Returns:
        float: the number of seconds
    """
    start = time.perf_counter()
    result = wait_n(n, max_delay)
    asyncio.run(result)
    end = time.perf_counter()
    elapsed = end - start
    return elapsed / n
