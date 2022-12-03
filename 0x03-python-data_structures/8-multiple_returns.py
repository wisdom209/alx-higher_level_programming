#!/usr/bin/python3
def multiple_returns(sentence):
    """function that returns a tuple with the length of a string and
    its first character.

    Args:
        sentence (string): string to get needed info from

    Returns:
        tuple: contains length of string and its first character
    """
    sentence_len = len(sentence)
    if (sentence_len == 0):
        return (0, None)
    return (sentence_len, sentence[0])
