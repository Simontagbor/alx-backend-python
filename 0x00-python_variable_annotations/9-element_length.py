#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function takes a list lst
    of strings and returns a list of"""
    return [(i, len(i)) for i in lst]
