#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """function that deletes the item at a specific position in a list

    Args:
        my_list (list, optional): list to delete element at given index.
        Defaults to [].
        idx (int, optional): index of element in my_list to remove.
        Defaults to 0.

    Returns:
        list: modified list
    """
    list_len = len(my_list)

    if (idx < 0 or idx >= list_len):
        pass
    else:
        for i in range(len(my_list)):
            if (i == idx):
                del (my_list[i])
    return my_list
