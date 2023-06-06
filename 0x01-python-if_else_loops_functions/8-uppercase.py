#!/usr/bin/python3
# 8-uppercase.py


def uppercase(string):
    """Print a string in uppercase."""
    result = ""
    for c in string:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        result += c
    print(result)
