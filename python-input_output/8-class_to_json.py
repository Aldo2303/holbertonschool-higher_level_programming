#!/usr/bin/python3
"""Module 8-class_to_json"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    argument:
        obj: is an instance of a Class
        Return: __dict__
    """
    return (obj.__dict__)
