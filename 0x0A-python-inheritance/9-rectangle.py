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
