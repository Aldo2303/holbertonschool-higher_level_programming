#!/usr/bin/python3
"""Module 8-rectangle
I can import the geometric base class in the following way:"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class that inherits from BaseGeometry
    Private method: width
    Private method: height
    """
    def __init__(self, width, height):
        """
        method that builds a rectangle and used interger_validator
        arguments:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
