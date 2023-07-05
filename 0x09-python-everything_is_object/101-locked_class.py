#!/usr/bin/python3
# 101-locked_class.py

"""Defines locked class."""


class LockedClass:
    """
    Prevent user from instant new Locked-Class attributes
    for all but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
