#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Create an instance of class Square"""
    def __init__(self, size=0):
        """
        Initializes Square
        Atributtes: size: size of square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
