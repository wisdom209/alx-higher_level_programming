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
