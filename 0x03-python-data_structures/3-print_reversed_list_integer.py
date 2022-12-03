#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print reversed list

    Args:
        my_list (list, optional): List to reverse. Defaults to [].
    """
    if (my_list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
