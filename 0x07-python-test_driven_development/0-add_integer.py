#!/usr/bin/python3
"""Arithmetic function"""


def add_integer(a, b=98):
    """Function adds 2 integers"""
    result = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
