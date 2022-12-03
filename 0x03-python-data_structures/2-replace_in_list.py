#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace element at given index

    Args:
        my_list (list): list
        idx (int): index of element
        element (any): element

    Returns:
        list: modified list
    """
    if (idx >= len(my_list) or idx < 0):
        return my_list
    my_list[idx] = element
    return my_list
