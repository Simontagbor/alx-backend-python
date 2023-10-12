#!/usr/bin/env python3
"""
A simple Module that defines a function for returning an asyncio task

Function:
    task_wait_random(max_delay: int)
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creates an asyncio task

    Args:
        max_delay (int): the number of seconds to delay by

    Returns:
        an instance of asyncio.Task

    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
