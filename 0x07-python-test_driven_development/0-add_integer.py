#!/usr/bin/python3
"""Adds 2 integers module"""


def add_integer(a, b=98):
    """function that adds 2 integers

    Args:
        a: integer
        b: integer

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
