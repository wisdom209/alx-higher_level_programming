#!/usr/bin/python3
"""module adds new attribute to object if possible"""


def add_attribute(new_class, key, value):
    """adds attribute to a class if possible
    """
    if hasattr(new_class, '__dict__'):
        setattr(new_class, key, value)
    else:
        raise TypeError("can't add new attribute")
