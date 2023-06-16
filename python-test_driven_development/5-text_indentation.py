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
    
    flag = 0
    no_print_space = ""
    for letter in range(len(text)):
        print(text[letter], end="")
        if text[letter] == "." or text[letter] == "?" or text[letter] == ":":
            flag = 1
        elif flag == 1:
            if text[letter] == " ":
                no_print_space = "".join(text[letter])
                print(no_print_space)
                print()
            flag = 0
