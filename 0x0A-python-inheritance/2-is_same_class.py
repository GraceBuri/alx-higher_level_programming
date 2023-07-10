#!/usr/bin/python3
"""returns True if object is an instance of the class"""


def is_same_class(obj, a_class):
    """returns True if object is a class instance
    Args: obj - object to check
          a_class - Class to check match
    """
    if type(obj) == a_class:
        return True
    else:
        return False
