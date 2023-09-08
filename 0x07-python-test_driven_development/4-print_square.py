#!/usr/bin/python3
"""Print square Module"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size: the size length of the square
    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    square = int(size)
    for _ in range(square):
        print("#" * square)
