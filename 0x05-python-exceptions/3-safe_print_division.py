#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide without exceptions

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: a/b
    """
    num = None
    try:
        num = a/b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(num))
    return num
