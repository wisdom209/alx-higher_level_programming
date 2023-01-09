#!/usr/bin/python3
"""Implements a function that detects a subclass
    """


def inherits_from(obj, a_class):
    """is obj a subclass of a_class

    Args:
        obj (any): Object
        a_class (any): Class

    Returns:
        bool: True if obj is a subclass of a_class
    """
    if (issubclass(obj.__class__, a_class) and type(obj) is not a_class):
        return True
    return False
