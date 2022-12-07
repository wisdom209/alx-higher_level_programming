#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Function that returns a set of common elements in two sets

    Args:
        set_1 (set): first set
        set_2 (set): second set

    Returns:
        set: intersection of set_1 and set_2
    """
    return set(set_1).intersection(set_2)
