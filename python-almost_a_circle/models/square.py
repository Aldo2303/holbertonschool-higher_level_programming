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