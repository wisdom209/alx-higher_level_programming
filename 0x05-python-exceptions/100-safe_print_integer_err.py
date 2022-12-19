#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer without Exceptions

    Args:
        value (int): Should be an integer

    Returns:
        Boolean: True if there is no exception
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        err = err.args[0]
        sys.stderr.write("Exception: " + err + "\n")
        return False
