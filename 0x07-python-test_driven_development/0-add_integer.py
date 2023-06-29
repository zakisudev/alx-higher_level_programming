#!/usr/bin/python3
"""
The "0-add_integer" module
This module calculates the sum of two numbers 'a' and 'b'
The 0-add_integer module has only one function add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    This function adds two integers
    """
    if not isinstance(a, (int, float)) or type(a) is bool:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or type(b) is bool:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
