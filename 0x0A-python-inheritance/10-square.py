#!/usr/bin/python3
"""10. Square #1 TASK"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size):
        """
        instatiation with size

        Args:
            size: square's size
        """
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """override area method"""
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {0}/{0}".format(self.__size)
