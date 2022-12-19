#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise an exception with a message

    Args:
        message (str, optional): Error message. Defaults to "".

    Raises:
        NameError: Exception raised
    """
    raise NameError(message)
