#!/usr/bin/python3
"""
A module that sets size of square as private field

"""


class Square:
    """Square class

    private instance field(s) : size
    methods: __init__

    """

    def __init__(self, size=0):
        """initializes the class

        Args:
            size (int, optional): size of square. Defaults to 0.
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
