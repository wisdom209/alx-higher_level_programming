#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as err:
        err = err.args[0]
        sys.stderr.write("Exception: " + err + "\n")

    return result
