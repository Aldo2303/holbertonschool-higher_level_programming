#!/usr/bin/python3
"""
Module 4-print_square
created method that print square with #
"""


def print_square(size):
    """
    function that prints a square with the character #
    Argument:
        size:  is the size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for column in range(size):
        for row in range(size):
            print("#", end="")
        print()
