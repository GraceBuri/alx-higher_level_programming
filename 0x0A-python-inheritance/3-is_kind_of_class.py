#!/usr/bin/python3
"""return true if object is an instance otherwise false"""


def is_kind_of_class(obj, a_class):
    """check is object is instance or inherited instance
    Args:
    obj - object to check
    a_class - classs to match obj
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
