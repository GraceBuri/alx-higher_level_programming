#!/usr/bin/python3
"""a module for the function read_file"""


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
