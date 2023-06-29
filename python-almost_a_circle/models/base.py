#!/usr/bin/python3
"""
Module 1-class_base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        adding the static method: def to_json_string(list_dictionaries)
        Return:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
