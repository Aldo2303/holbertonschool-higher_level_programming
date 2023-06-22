#!/usr/bin/python3
"""Module 1-my_list"""


class MyList(list):
    """
    class my list that inherits from list
    """
    def print_sorted(self):
        """
        print list ascending sorted
        """
        ordered_list = sorted(self)
        print(ordered_list)
