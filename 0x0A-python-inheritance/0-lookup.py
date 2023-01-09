#!/usr/bin/python3
"""Prints methods of a class"""


def lookup(obj):
    """prints the attributes of an object

    Args:
            obj (any): object
    """
    dir(obj)

lookup(int)
