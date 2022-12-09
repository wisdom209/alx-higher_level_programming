#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes all values equal to given value
    in python dictionary

    Args:
        a_dictionary (dict): dictionary to delete from
        value (any): value in a dictionary

    Returns:
        dict: modified dictionary
    """
    del_key_list = []
    if len(a_dictionary) > 0 and isinstance(a_dictionary, dict):
        for k, v in a_dictionary.items():
            if (v == value):
                del_key_list.append(k)
    for i in del_key_list:
        del (a_dictionary[i])
    return a_dictionary
