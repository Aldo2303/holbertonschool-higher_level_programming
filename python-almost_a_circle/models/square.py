#!/usr/bin/python3
"""
Module 3-class_square
"""
from models.rectangle import Rectangle
"""
import class Rectangle
"""


class Square(Rectangle):
    """
     inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class contructor of square
        arg:
            size (size for width and size for height)
            x
            y
            id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Update the class square
        overriding the __str__ method
        Return:
            [Square] (<id>) <x>/<y> - <size>
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width))

    @property
    def size(self):
        """
        getter
        Return:
            size of square
        """
        return (self.width)

    @size.setter
    def size(self, size):
        """
        setter
        attribute:
            size of square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Public method: def update(self, *args and **kwars)
        that assigns an argument to each attribute
        arg: list of arguments
        """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Public method: def to_dictionary(self)
        Return:
            the dictionary representation of a Square
        """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return (dictionary)
