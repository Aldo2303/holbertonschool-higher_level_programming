#!/usr/bin/python3
"""Module 9-student"""


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

    def to_json(self):
        """
        Return:
            dictionary representation of a Student instance
        """
        return (self.__dict__)
