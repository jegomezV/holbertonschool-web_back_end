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
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Funct to multiply"""
    return lambda x: x * multiplier
