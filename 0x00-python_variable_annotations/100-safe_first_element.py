#!/usr/bin/env python3
"""This module contains the function for task 100"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """This function returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
