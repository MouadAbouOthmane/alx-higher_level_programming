#!/usr/bin/python3
"""1. My list TASK"""


class MyList(list):
    """
    a class MyList that inherits from list
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
