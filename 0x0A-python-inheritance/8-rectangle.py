#!/usr/bin/python3
"""8. Rectangle TASK"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        instatiation with width and height

        Args:
            width: rectangle's width
            height: rectangle's height
        """
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)
