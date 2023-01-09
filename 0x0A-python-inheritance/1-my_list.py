#!/usr/bin/python3
"""My list class
    """


class MyList(list):
    """Derived class of list

    Args:
            list (list): List Class
    """

    def __init__(self):
        """initiates the class
        """
        super().__init__()

    def print_sorted(self):
        """prints the sorted list
        """
        newlist = self[:]
        newlist.sort()
        print(newlist)
