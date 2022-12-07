#!/usr/bin/python3
def best_score(a_dictionary):
    """Get max integer value in a dictionary

    Args:
        a_dictionary (dict): dictionary

    Returns:
        int: max integer
    """
    return sorted(a_dictionary.items(), reverse=True, key=lambda x: x[1])[0][1]
