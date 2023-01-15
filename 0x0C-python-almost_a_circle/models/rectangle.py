#!/usr/bin/python3
"""This module implements Rectangle class"""
from .base import Base


class Rectangle(Base):
    "Rectangle class implementation"

    def __init__(self, width, height, x=0, y=0, id=None):
        "Class initialization constructor"
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates area of a rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints to stdout the rectangle instance"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Prints informal string representation of rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" + " - " + \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        tuple_range = len(args)
        if tuple_range < 1:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                if type(kwargs['width']) is not int:
                    raise (TypeError("width must be an integer"))
                if kwargs['width'] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = kwargs['width']
            if 'height' in kwargs:
                if type(kwargs['height']) is not int:
                    raise (TypeError("height must be an integer"))
                if kwargs["height"] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = kwargs['height']
            if 'x' in kwargs:
                if type(kwargs['x']) is not int:
                    raise TypeError("x must be an integer")
                if kwargs['x'] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = kwargs['x']
            if 'y' in kwargs:
                if type(kwargs['y']) is not int:
                    raise TypeError("y must be an integer")
                if kwargs['y'] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = kwargs['y']
        else:
            if (tuple_range >= 1):
                self.id = args[0]
            if (tuple_range >= 2):
                if type(args[1]) is not int:
                    raise (TypeError("width must be an integer"))
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = args[1]
            if (tuple_range >= 3):
                if type(args[2]) is not int:
                    raise (TypeError("height must be an integer"))
                if args[2] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = args[2]
            if (tuple_range >= 4):
                if type(args[3]) is not int:
                    raise TypeError("x must be an integer")
                if args[3] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[3]
            if (tuple_range >= 5):
                if type(args[4]) is not int:
                    raise TypeError("y must be an integer")
                if args[4] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[4]

    def to_dictionary(self):
        """returns dict representation of rectangle"""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
