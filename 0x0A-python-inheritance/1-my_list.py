#!/usr/bin/python3
"""subclass inheriting"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
