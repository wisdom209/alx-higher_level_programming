#!/usr/bin/python3
"""Module implements a function that returns True
if the object is an instance of,
or if the object is an instance of a class
that inherited from,
the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """Same class or inherits from

    Args:
        obj (any): Object
        a_class (any): class

    Returns:
        bool: True if same class or inherits from class
    """
    if (isinstance(obj, a_class) or issubclass(obj.__class__, a_class)):
        return True
    return False
