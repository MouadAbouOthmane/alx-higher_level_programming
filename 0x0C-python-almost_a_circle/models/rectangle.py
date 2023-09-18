#!/usr/bin/python3
"""2. First Rectangle TASK """
from models.base import Base
# Base = __import__('base').Base



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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x property"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y property"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle with the character #"""
        print('\n' * self.__y, end="")
        for _ in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def __str__(self):
        """__str__ method """
        return "[Rectangle] (" \
            + f"{self.id}) {self.__x}/{self.__y} - "\
            + f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update the argument of instance"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 
                'id': self.id, 'height': self.__height, 'width': self.__width}
