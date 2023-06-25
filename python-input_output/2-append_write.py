#!/usr/bin/python3
"""Module 2-append_write_file"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file (UTF8)
    Arguments:
        filename: file to be read
        text: text for added
    Return:
        the number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(text))
