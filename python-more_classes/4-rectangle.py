#!/usr/bin/python3
"""
Module 0-rectangle
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    defined class Rectangle with private attributes width and height
    Attributes:
        width: the width of Rectangle
        height: The height of Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialized an instance of class Rectangle
        Arguments:
            width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """
        Calculates the area of rectangle
        Return:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of rectangle
        Return:
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Prints rectangle with #
        Return:
            the rectangle printed if width and height > 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        resu = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return resu

    def __repr__(self):
        """
        method return a more information-rich, or official, string of an object
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
