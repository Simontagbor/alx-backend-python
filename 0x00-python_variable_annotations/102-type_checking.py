#!/usr/bin/env python3
"""This module contains the function for task 12"""
from typing import Tuple, List


def zoom_array(
    lst: Tuple[int, ...],
    factor: int = 2
) -> Tuple[int, ...]:
    """This function returns a tuple"""
    zoomed_in: Tuple[int, ...] = tuple(
        item
        for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
