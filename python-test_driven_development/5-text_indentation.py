#!/usr/bin/python3
"""
Module 5-text_indentation
method for indentation
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Argument:
        text: text to be printed, applying the changes
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    char_before = 0
    for i in range(len(text)):
        if char_before is 1:
            char_before = 0
            if text[i] == " ":
                continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            char_before = 1
