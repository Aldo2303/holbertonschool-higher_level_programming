#!/usr/bin/python3
"""Module 10-student"""


class Student:
    """
    built class student
    Public Attributes:
        first_name
        last_name
        age
    Public Method:
        def to_json(self): that retrieves a dictionary representation
        of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialized student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        argument:
            attrs
        Return:
            dictionary representation of a Student instance
        """
        if attrs is None:
            return (self.__dict__)
        else:
            dictionary = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    dictionary[i] = self.__dict__[i]
            return (dictionary)

    def reload_from_json(self, json):
        """
        argument:
            json
        """
        self.first_name = json.get("fisrt_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
