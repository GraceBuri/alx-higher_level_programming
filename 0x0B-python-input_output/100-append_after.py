#!/usr/bin/python3
"""define an inster function"""


def append_after(filename="", search_string="", new_string=""):
    """insert text at a specific line function"""
    string = ""
    with open(filenme, "r") as f:
        for line in file:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, "w") as f:
        file.write(string)
