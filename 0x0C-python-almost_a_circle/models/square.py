#!/usr/bin/python3
"""This module implements the square class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class implementation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class initialization constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints informal string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y}" + " - " + \
            f"{self.width}"

    @property
    def size(self):
        """square size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """square size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes of square class"""
        tuple_range = len(args)

        if (tuple_range <= 0):
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        else:
            if tuple_range >= 1:
                self.id = args[0]
            if tuple_range >= 2:
                self.size = args[1]
            if tuple_range >= 3:
                self.x = args[2]
            if tuple_range >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """Returns a dict representation of the square"""

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
