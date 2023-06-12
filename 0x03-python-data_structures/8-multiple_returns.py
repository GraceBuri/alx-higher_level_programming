#!/usr/bin/python3
# 4-print_sorted_list.py

def print_sorted_list(my_list=[]):
    """Print a list in ascending order."""
    sorted_list = sorted(my_list)
    for i in sorted_list:
        print("{:d}".format(i))
