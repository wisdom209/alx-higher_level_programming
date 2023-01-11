#!/usr/bin/python3
"""I/0 module"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, "r", encoding="UTF-8") as f:
        content = f.read()
        if (content[-1] == '\n'):
            content = content[:-1]
        print(content)
