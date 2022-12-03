#!/usr/bin/python3
def max_integer(my_list=[]):
    """Gets the largest integer in a list of integers

    Args:
        my_list (list, optional): list of integers. Defaults to [].

    Returns:
        integer: largest integer in my_list
    """
    list_len = len(my_list)
    max = float('-inf')

    if (list_len == 0):
        return None
    for i in my_list:
        if (i >= max):
            max = i
    return max
