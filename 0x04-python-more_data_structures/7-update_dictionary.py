#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds key/value in a dictionary

    Args:
            a_dictionary (dict): _description_
            key (string): key
            value (any): value

    Returns:
            dict: modified dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
