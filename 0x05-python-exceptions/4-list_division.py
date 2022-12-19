#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divide values at corresponding indices and return new list

    Args:
        my_list_1 (list): First List
        my_list_2 (list): Second List
        list_length (int): Length of new list

    Returns:
        list: New list from division of elements of two lists
    """
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i]/my_list_2[i])
        except (IndexError):
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        finally:
            continue

    return new_list
