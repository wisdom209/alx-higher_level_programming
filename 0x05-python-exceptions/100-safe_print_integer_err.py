#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        err = err.args[0]
        sys.stderr.write("Exception: " + err + "\n")
        return False
