#!/usr/bin/python3
"""Module 6-base_geometry"""


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
