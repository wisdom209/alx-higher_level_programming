#!/usr/bin/python3
"""read a text file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename, "r") as file:
        content = file.read()
        print(content)
