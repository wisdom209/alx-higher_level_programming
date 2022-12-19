#!/usr/bin/python3

def safe_print_integer(value):
    """Print only integer values

    Args:
        value (any): Value to print

    Returns:
        Boolean: True if value is an integer
    """
    try:
        print("{:d}".format(value))
    except ValueError as err:
        return False
    except Exception as err:
        return False
    return True
