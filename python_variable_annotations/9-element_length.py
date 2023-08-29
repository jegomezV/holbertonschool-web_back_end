#!/usr/bin/env python3
"""
|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
| Module:                                                      |
|8-make_multiplier.py                                          |
|                                                              |
|Description:                                                  |
|Write a type-annotated function make_multiplier               |
|that takes a float multiplier as argument                     |
|and returns a function that multiplies a float by multiplier. |
|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return any"""
    return [(i, len(i)) for i in lst]
