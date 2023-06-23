#!/usr/bin/python3
"""
Module 10-square
Import the class rectangle, this is a subclass of the class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a subclass of the class BaseGeometry
    Method Private:
        __init__(self, size)
    """
    def __init__(self, size):
        """
        method: size that builds a square and used interger_validator
        argument private:
            size: contains 2 arguments (width and height) of area the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
