#!/usr/bin/python3
"""10. And now, the Square! TASK """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        instatiation

        Args:
            size: rectangle size
            x: rectangle axis x
            y: rectangle axis y
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ method """
        return "[Square] (" \
            + f"{self.id}) {self.x}/{self.y} - "\
            + f"{self.size}"

    def update(self, *args, **kwargs):
        """update the argument of instance"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of a Rectangle:"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
