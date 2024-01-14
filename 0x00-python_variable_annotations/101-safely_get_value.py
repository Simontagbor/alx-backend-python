#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import TypeVar, Dict
from typing import Union, Mapping, Any

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return value of key or default"""
    if key in dct:
        return dct[key]
    else:
        return default
