#!/usr/bin/python3
"""returns true if object is a class instance else false"""


def inherits_from(obj, a_class):
    """checks if object is inherited or an instance
    Args:
    obj - obj to check
    a_class - class to match obj
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
