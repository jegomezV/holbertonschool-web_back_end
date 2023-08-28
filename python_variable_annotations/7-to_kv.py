#!/usr/bin/env python3
"""
|- - - - - - - - - - - - - - - - - - - - - - - - - - |
| Module:                                            |
|6-sum_mixed_list.py                                 |
|                                                    |
|Description:                                        |
|Write a type-annotated function sum_mixed_list      |
|which takes a list mxd_lst of integers and floats   |
|and returns their sum as a float.                   |
|- - - - - - - - - - - - - - - - - - - - - - - - - - |
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Funct to return a tuple[Str, Float]"""
    return (k, v*v)
