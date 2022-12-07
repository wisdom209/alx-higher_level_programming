#!/usr/bin/python3
def best_score(a_dictionary):
    """Get max integer value in a dictionary

    Args:
        a_dictionary (dict): dictionary

    Returns:
        int: max integer
    """
    if (a_dictionary):
        return sorted([k for k, v in a_dictionary.items()], reverse=True)[0]

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
