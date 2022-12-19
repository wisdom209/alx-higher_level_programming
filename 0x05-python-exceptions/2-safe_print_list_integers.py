#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print only integers in list

    Args:
        my_list (list, optional): List of elements. Defaults to [].
        x (int, optional): list length. Defaults to 0.

    Returns:
        int: number of integers printed
    """
    num_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except ValueError:
            continue
        except TypeError:
            continue
        except NameError:
            continue
    print()
    return num_printed
