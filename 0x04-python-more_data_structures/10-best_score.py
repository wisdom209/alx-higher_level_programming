#!/usr/bin/python3
def best_score(a_dictionary):
    """Get max integer value in a dictionary

    Args:
        a_dictionary (dict): dictionary

    Returns:
        int: max integer
    """
    if (a_dictionary):
        return sorted([k for k in a_dictionary.keys()], reverse=True)[0]
