#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Function that replaces all occurrences
        of an element by another in a new list

    Args:
            my_list (list): List to work on
            search (any): Element to search and replace
            replace (any): Element to replace search with

    Returns:
            list: modified list
    """

    return list(map(lambda x: replace if x == search else x, my_list))
