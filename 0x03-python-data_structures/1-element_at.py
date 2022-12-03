#!/usr/bin/python3
def element_at(my_list, idx):
    """Returns element at given index

    Args:
        my_list (list): list
        idx (integer): index of element

    Returns:
        any: element at idx
    """
    if (idx < 0):
        return None
    if (idx >= len(my_list)):
        return None
    return (my_list[idx])
