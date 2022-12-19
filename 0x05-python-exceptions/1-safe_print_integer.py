#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        return False
    except Exception as err:
        return False
    return True
