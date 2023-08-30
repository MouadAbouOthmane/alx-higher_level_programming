#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""
	
    def __init__(self, size = 0):
        """initialization method

        Args:
            size: size of square.
        """
        self.size = size

    @property
    def size(self):
        """property of size of square
        
        Raises:
            TypeError: size must be an integer.
            ValueError: if size is less than 0.
        """
        return self.__size
        
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of square

        Returns:
             Current square area.
        """
        return self.__size ** 2
