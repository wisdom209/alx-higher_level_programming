#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Function that adds all unique integers
        in a list (only once for each integer

    Args:
            my_list (list, optional): List of integers. Defaults to [].

    Returns:
            int: sum of unique integers in my_list
    """

    if my_list:
        my_list = set(my_list)
        uniq_sum = 0
        for x in my_list:
            uniq_sum += x
        return (uniq_sum)
    else:
        return 0
