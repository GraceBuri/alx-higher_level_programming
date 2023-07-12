#!/usr/bin/python3
""" Module that contains a function that appends to a text file"""


def append_write(filename="", text=""):
    """appends gicen text at end of file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
