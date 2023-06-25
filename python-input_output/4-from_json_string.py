#!/usr/bin/python3
"""Module 4-from_json_string"""
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    argument:
        my_str
    Return:
        sn object in Python data structure
    """
    return (json.loads(my_str))
