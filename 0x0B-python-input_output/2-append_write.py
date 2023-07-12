#!/usr/bin/python3
""" Module that contains a function that appends to a text file"""


def append_write(filename="", text=""):
    try:
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        raise e
