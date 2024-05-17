#!/usr/bin/python3
"""
This is the add_integer module.

This module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b.

    Args:
        a (int, float): the first value.
        b (int, float): the second value.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
