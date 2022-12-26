#!/usr/bin/python3
"""This module prints a text with 2 new lines after each of these
characters: ., ? and :"""
import doctest


def text_indentation(text):
    """This module prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): string to print

    Raises:
        TypeError: test must be a string
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")

    i = 0
    for _ in range(len(text)):
        print(text[i], end="")

        if (text[i] == "." or text[i] == "?" or text[i] == ":"):
            if (text[i + 1] == " "):
                i += 1
                while (text[i] == " "):
                    i += 1
            print()
            print()
        else:
            i += 1
        if (i == len(text) - 1):
            break


if __name__ == '__main__':
    doctest.testfile("./tests/5-text_indentation.txt")
