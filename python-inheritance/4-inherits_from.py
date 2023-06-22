#!/usr/bin/python3
"""Module 2-is_same_class.py"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    Return:
        True if obj issubclass() of a_class
    """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
