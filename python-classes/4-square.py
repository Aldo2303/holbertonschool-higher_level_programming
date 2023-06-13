#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Create an instance of class Square"""
    def __init__(self, size=0):
        """
        Initializes Square
        Atributtes: size: size of square
        """
        self.size = size

    @property
    def size(self):
        """
        getter
        Return:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter
        atributtes:
            value, the new size
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public instance method
        Return:
            the current square area
        """
        return self.__size * self.__size
