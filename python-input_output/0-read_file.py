#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8)
    and prints it to stdout:
    argument:
        filename: file to be read
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
