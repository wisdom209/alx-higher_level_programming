#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary (dict): dictionary to modify

    Returns:
        dict: modified dictionary
    """
    return {k: (v * 2) for k, v in a_dictionary.items()}
