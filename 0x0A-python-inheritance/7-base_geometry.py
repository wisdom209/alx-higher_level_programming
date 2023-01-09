#!/usr/bin/python3
"""This module implements a Geometry class
    """


class BaseGeometry:
    """A Base Geometry class
    """

    def area(self):
        """Base geometry area function

            Raises:
                    Exception: area() is not implemented
            """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer

        Args:
            name (string): "String description"
            value (int): integer representation

        Raises:
            TypeError: {name} must be an integer"
            TypeError: "{name} must be greater than 0"
        """
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value < 1):
            raise ValueError(f"{name} must be greater than 0")
