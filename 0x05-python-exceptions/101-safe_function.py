#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Run a function and print exceptions

    Args:
        fct (args): Tuple argument to function

    Returns:
        any: Return value of function fct
    """
    result = None
    try:
        result = fct(*args)
    except Exception as err:
        err = err.args[0]
        sys.stderr.write("Exception: " + err + "\n")

    return result
