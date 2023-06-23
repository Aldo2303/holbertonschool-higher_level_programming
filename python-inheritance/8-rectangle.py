#!/usr/bin/python3
"""Module 8-rectangle
I can import the geometric base class in the following way:
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""


class BaseGeometry:
    """
    Public method: area
    Public method: integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that check if value is an int and is >0
        arguments:
            name: is always a string
            value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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
