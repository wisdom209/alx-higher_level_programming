#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Function that returns a set of
    all elements present in only one set

    Args:
        set_1 (set): set 1
        set_2 (set): set 2

    Returns:
        set: set containing elements not intersecting
    """
    return set(set_1 - set_2).union(set_2 - set_1)
