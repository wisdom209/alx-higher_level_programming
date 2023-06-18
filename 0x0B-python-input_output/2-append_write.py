#!/usr/bin/python3
"""append text module"""


def append_write(filename="", text=""):
    """append function"""
    with open(filename, "a") as file:
        return file.write(text)
