#!/usr/bin/python3
def no_c(my_string):
    new_copy = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_copy += i
    return (new_copy)
