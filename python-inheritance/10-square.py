#!/usr/bin/python3
"""
Module 10-square
Import the class rectangle, this is a subclass of the class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a subclass of the class BaseGeometry
    Private method: size
    """
    def __init__(self, size):
        """
        method that builds a square and used interger_validator
        argument:
            size: contains 2 arguments (width and height) of area the square
        """
        width = size
        height = size
        super().__init__(width, height)
        self.integer_validator("size", size)
        self.__size = size