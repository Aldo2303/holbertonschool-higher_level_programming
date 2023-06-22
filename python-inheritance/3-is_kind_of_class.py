#!/usr/bin/python3
"""Module 2-is_same_class.py"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
    Return:
        True if obj isinstance a class
    """
    return (isinstance(obj, a_class))
