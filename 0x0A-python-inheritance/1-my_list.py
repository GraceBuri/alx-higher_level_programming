#!/usr/bin/python3
"""class myList inherits from class list"""


class MyList(list):
    """mylist inherits from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
