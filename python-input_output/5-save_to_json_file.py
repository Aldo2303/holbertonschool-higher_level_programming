#!/usr/bin/python3
"""Module 5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file
    using a JSON representation
    arguments:
        my_obj
        filename
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
