#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = ""
    for char in my_string:
        if char.lower() != 'c':
            copy += char
    return copy
