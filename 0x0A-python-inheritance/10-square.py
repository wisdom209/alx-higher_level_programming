#!/usr/bin/python3
"""This module implements a square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class

    Args:
            Rectangle (Rectangle): Base Class
    """
    def __init__(self, size):
        """initializes the Square class

        Args:
                size (int): square width
        """
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Gets area of a square

        Returns:
                int: Area of square
        """
        return self.__size ** 2
