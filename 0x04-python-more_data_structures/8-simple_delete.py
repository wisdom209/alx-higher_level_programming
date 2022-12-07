#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """delete a key in a dictionary

    Args:
            a_dictionary (dict): dictionary to modify
            key (str, optional): key. Defaults to "".

    Returns:
            dict: modified dictionary
    """
    if key in a_dictionary.keys():
        del (a_dictionary[key])
    return a_dictionary
