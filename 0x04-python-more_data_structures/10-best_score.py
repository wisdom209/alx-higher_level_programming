#!/usr/bin/python3
def best_score(a_dictionary):
    """Get max integer value in a dictionary

    Args:
        a_dictionary (dict): dictionary

    Returns:
        int: max integer
    """
    if (a_dictionary):
        d = sorted(a_dictionary.items(), reverse=True, key=lambda x: x[1])
        return d[0][0]
