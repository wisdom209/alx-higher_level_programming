#!/usr/bin/python3
"""
This module prints a name
"""
import doctest


def say_my_name(first_name, last_name=""):
    """Print My name is <first_name> <last_name>

    Args:
            first_name (str): First name
            last_name (str, optional): Last name. Defaults to "".
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")

    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == '__main__':
    doctest.testfile("./tests/3-say_my_name.txt")
