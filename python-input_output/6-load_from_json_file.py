#!/usr/bin/python3
"""Module 5-save_to_json_file"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    argument:
        filename
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        json_obj = file.read()
        python_obj = json.loads(json_obj)
        return (python_obj)
