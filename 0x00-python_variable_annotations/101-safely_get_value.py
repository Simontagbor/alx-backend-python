#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import TypeVar, Dict


KT = TypeVar('KT')
VT = TypeVar('VT')


def safely_get_value(dct: Dict[KT, VT], key: KT, default: VT = None) -> VT:
    if key in dct:
        return dct[key]
    else:
        return default
