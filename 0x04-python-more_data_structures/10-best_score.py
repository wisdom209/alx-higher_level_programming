#!/usr/bin/python3
def best_score(a_dictionary):
    """Get max integer value in a dictionary

    Args:
        a_dictionary (dict): dictionary

    Returns:
        int: max integer
    """
    if (a_dictionary):
        return sorted([v for k, v in a_dictionary.items()], reverse=True)
