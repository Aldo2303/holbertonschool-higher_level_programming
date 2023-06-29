#!/usr/bin/python3
"""
Module 2-class_rectangle
"""
from models.base import Base
"""
import class Base
"""


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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, height):
        """
        setter
        attribute:
            height of rectangle
        """
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, x):
        """
        setter
        attribute:
            x for rectangle
        """
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, y):
        """
        setter
        attribute:
            y for rectangle
        """
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        public method: def area(self)
        Return:
            Area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Update the class Rectangle
        public method: def display(self)
        that prints in stdout the Rectangle instance with the character #
        """
        for a in range(self.__y):
            print()
        for column in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Update the class Rectangle
        overriding the __str__ method
        Return:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Public method: def update(self, *args)
        that assigns an argument to each attribute
        arg: list of arguments
        """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        Public method: def to_dictionary(self)
        Return:
            the dictionary representation of a Rectangle
        """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.__width
        dictionary["height"] = self.__height
        dictionary["x"] = self.__x
        dictionary["y"] = self.__y
        return (dictionary)
