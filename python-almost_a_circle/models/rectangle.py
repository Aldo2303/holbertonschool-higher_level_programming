#!/usr/bin/python3
"""
Module 2-class_rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Private instance attributes:
        __width
        __height
        __x
        __y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class contructor of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            getter
            Return:
                width of rectangle
            """
            return (self.__width)

        @property
        def height(self):
            """
            getter
            Return:
                height of rectangle
            """
            return (self.__height)

        @property
        def x(self):
            """
            getter
            Return:
                x for rectangle
            """
            return (self.__x)

        @property
        def y(self):
            """
            getter
            Return:
                y for rectangle
            """
            return (self.__y)

        @width.setter
        def width(self, width):
            """
            setter
            attribute:
                width of rectangle
            """
            self.__width = width

        @height.setter
        def width(self, height):
            """
            setter
            attribute:
                height of rectangle
            """
            self.__height = height

        @x.setter
        def width(self, x):
            """
            setter
            attribute:
                x for rectangle
            """
            self.__x = x

        @y.setter
        def width(self, y):
            """
            setter
            attribute:
                y for rectangle
            """
            self.__y = y
