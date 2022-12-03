#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints integers in a list

    Args:
        my_list (list, optional): Prints integers in a list. Defaults to [].
    """
    for i in range(len(my_list)):
        print('{:d}'.format(my_list[i]))
