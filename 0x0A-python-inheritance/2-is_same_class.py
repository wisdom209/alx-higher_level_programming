#!/usr/bin/python3
"""This module checks if too classes are same
    """


def is_same_class(obj, a_class):
    """check if two objects are of same class

    Args:
        obj (any): an object
        a_class (any): an object

    Returns:
        bool: True if same class, False if otherwise
    """
    if (type(obj) is a_class):
        return True
    return False
