#!/usr/bin/python3
"""7. Integer validator TASK"""


class BaseGeometry:
    """
    Geometry class
    """

    def area(self):
        """
        Raise an exception

        Raises:
            Exception: area() is not implement
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates value

        Args:
            name: a string
            value: must be an ineger
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
