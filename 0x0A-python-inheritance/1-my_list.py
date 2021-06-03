#!/usr/bin/python3
"""
A class MyList that inherits from list:
"""


class MyList(list):
    """class MyList docstring"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
