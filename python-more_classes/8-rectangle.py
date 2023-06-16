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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialized an instance of class Rectangle
        Arguments:
            width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        symbol = str(self.print_symbol)
        resu = "\n".join([symbol * self.__width for i in range(self.__height)])
        return resu

    def __repr__(self):
        """
        method return a more information-rich, or official, string of an object
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
        """
        INSTEAD of AREA, you could have used the PERIMETER function:
        if rect_1.perimeter() >= rect_2.perimeter():
            return rect_1
        return rect_2
        """
