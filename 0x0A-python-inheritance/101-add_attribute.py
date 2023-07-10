#!/usr/bin/python3
"""add new attribute to object"""


def add_attribute(obj, attribute, value):
    """function adding a new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
