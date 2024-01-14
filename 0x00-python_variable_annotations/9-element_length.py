#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """This function takes a list lst
    of strings and returns a list of"""
    return [(i, len(i)) for i in lst]
