#!/usr/bin/python3
"""2. First Rectangle TASK """
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instatiation

        Args:
            width: rectangle width
            height: rectangle height
            x: rectangle axis x
            y: rectangle axis y
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
