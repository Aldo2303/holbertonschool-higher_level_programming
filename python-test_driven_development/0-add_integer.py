#!/usr/bin/python3
"""Module 0-add_interger"""


def add_integer(a, b=98):
    """
    function that adds 2 integers
    The values a and b must be int or float
    arguments:
        a and b
    Return:
        the addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
