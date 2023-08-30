#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method

        Args:
            size: size of square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property of position of square

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of square

        Returns:
             Current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """print square with character #
        """
        if self.size == 0:
            print()
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(end=" ")
            for _ in range(self.size):
                print("#", end="")
            print()
