#!/usr/bin/python3

def weight_average(my_list=[]):
    """Calculate weighted average of tuples in list

    Args:
        my_list (list, optional): list of integer
        tuples having value and weight. Defaults to [].

    Returns:
        int: weighted average of tuples in list
    """
    list_len = len(my_list)
    weight_sum = 0
    running_add = 0

    if (list_len == 0):
        return 0

    for value, weight in my_list:
        weight_sum += weight
        running_add += (value * weight)

    return running_add/weight_sum
