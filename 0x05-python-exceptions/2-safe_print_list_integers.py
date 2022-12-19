#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): print only integers in list. Defaults to [].
        x (int, optional): Length to print. Defaults to 0.

    Returns:
        int: Number of integers printed
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
