#!/usr/bin/python3
"""Rebel MyInt"""


class MyInt(int):
    """Implementation of of rebel int"""

    def __eq__(self, x):
        """Inverts equality"""
        return False

    def __ne__(self, x):
        """Inverts inequality"""
        return True
