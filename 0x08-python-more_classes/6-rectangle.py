#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Define a Rectangle"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialization method

        Args:
            width: width of square.
            height: height of square.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property of width of square.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of rectangle's height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area

        Return:
            the current rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Rectangle perimeter

        Return:
            the current rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for _ in range(self.__width):
                print("#", end='')
            if i != self.__height - 1:
                print("")
        return ""

    def __repr__(self):
        return "Rectangle("\
            + str(self.__width) + ", " \
            + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
