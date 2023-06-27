#!/usr/bin/python3
"""
Module 1-class_base
"""


class Base:
    """
    private class attribute:
        objects numbers: initialized in 0.
        Increment each time called to connstructor
    Meothod:
        __init__(self, id)
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        class constructor. assigns id when created a new object.
        arg:
            id: int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
