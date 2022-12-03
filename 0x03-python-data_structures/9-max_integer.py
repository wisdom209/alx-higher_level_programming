#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    max = float('-inf')

    if (list_len == 0):
        return None
    for i in my_list:
        if (i >= max):
            max = i
    return max
