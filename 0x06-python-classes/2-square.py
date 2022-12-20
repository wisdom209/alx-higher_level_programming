#!/usr/bin/python3
"""
_summary_

"""


class Square:
    """Square class

    private instance field(s) : size
    methods: __init__

    """

    def __init__(self, size=0):
        if (isinstance(size, int) and size < 0):
            raise (ValueError("size must be >=0"))
        elif (isinstance(size, int) is not True):
            raise (TypeError("size must be an integer"))
        else:
            self.__size = size
