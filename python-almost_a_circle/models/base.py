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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        adding the class method: def save_to_file(cls, list_objs)
        arg:
            list_obj: Writes JSON string represent of list_objs to a file:
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        result = []

        for object in list_objs:
            result.append(cls.to_dictionary(object))

        json_str = Base.to_json_string(result)

        with open(filename, mode="w", encoding="UTF-8") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        adding the static method: def from_json_string(json_string)
        arg:
            json_string
        Return:
            the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return ([])

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        adding the class method: def create(cls, **dictionary)
        arg:
            dictionary: **dictionary must be used **kwargs of the method update
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        adding the class method: def load_from_file(cls)
        Return:
            To a list of instances
        """
        filename = cls.__name__ + ".json"
        instances = []

        if (filename):
            with open(filename, mode="r", encoding="UTF-8") as file:
                json_str = cls.from_json_string(file.read())
                for inst in json_str:
                    instances.append(cls.create(**inst))
        return (instances)
