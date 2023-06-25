#!/usr/bin/python3
"""Module 1-write_file"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    Arguments:
        filename: file to be read
        text: text for writen
    Return:
        the number of characters written:
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
