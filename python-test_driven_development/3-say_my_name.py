#!/usr/bin/python3
"""Module 3-say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    Arguments:
        first_name, last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
