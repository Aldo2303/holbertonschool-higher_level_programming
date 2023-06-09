#!/usr/bin/python3
"""Module 10-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Import the class rectangle, this is a subclass of the class BaseGeometry.
    Method Private:
        __init__(self, size)
    """
    def __init__(self, size):
        """
        initializes size: That builds a square and used interger_validator
        argument private:
            size: contains 2 arguments (width and height) of area the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return: the object representation in a string format
        with class name, measure of width and height
        """
        return ("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                          self.__size, self.__size))
