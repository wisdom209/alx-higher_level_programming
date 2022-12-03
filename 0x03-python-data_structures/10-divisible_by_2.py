#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns list of integers divisible by 2

    Args:
        my_list (list, optional): list to filter. Defaults to [].

    Returns:
        list: integers form my_list that are divisible by 2
    """
    return [x % 2 == 0 for x in my_list]
