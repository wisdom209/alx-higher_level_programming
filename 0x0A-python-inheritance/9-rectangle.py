#!/usr/bin/python3
"""This module implements a Rectangle class
    """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """instantiate members of the class

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Gets area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of triangle

        Returns:
            str: String representation
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
