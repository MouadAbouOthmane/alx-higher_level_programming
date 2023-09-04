#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Define a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization method

        Args:
            width: width of square.
            height: height of square.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width of square.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """property of rectangle's height
        
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    def area(self):
        """Rectangle area
        
        Return:
            the current rectangle area 
        """
        return self.height * self.width

    def perimeter(self):
        """Rectangle perimeter

        Return:
            the current rectangle perimeter 
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2
