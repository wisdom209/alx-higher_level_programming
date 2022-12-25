#!/usr/bin/python3
"""This module prints a square with #
"""
import doctest


def print_square(size):
    """prints a square

    Args:
        size (int): width of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if (type(size) is float and size < 0):
        raise TypeError("size must be an integer")

    if (type(size) is not int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)


if __name__ == '__main__':
    doctest.testfile("./tests/4-print_square.txt")
