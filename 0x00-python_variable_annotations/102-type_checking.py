#!/usr/bin/env python3
"""This module contains the function for task 12"""
from typing import Tuple, List


def zoom_array(
    lst: Tuple,
    factor: int = 2
) -> List:
    """This function returns a list"""
    zoomed_in: List = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
