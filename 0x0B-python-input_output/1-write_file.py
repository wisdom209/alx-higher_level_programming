#!/usr/bin/python3
"""write to a file module"""


def write_file(filename="", text=""):
    """write to file function"""
    with open(filename, "w") as file:
        return file.write(text)
