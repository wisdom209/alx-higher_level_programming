#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary
    by ordered keys.

    Args:
        a_dictionary (dict): dictionary to sort
    """
    for x in sorted(a_dictionary.items()):
        print(f"{x[0]}: {x[1]}")
