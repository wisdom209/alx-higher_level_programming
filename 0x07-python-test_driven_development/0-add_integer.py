#!/usr/bin/python3
"""This module adds two integers"""
import doctest


def add_integer(a, b=98):
    """Adds a and b and returns result

    Args:
        a (int): `a`
        b (int, optional): `b`. Defaults to 98.

    Raises:
        TypeError: a must be an int
        TypeError: b must be an int

    Returns:
        int: `a` + `b`
    """
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    if (type(a) is not int):
        raise TypeError("a must be an integer")
    if (type(b) is not int):
        raise TypeError("b must be an integer")

    return a + b


if __name__ == '__main__':

    doctest.testfile("./tests/0-add_integer.txt")

    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
