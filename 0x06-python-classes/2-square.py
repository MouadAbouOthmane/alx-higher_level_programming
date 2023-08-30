#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """initialization method

        Args:
            size: size of square.

        Raises:
            TypeError: size must be an integer.
            ValueError: if size is less than 0.
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
