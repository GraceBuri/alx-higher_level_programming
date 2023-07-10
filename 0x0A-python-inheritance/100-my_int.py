#!/usr/bin/python3
"""define a class myInt inheriting from int"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverte"""
    def __eq__(self, value):
        return int(str(self)) != value

    def __ne__(self, value):
        return int(str(self)) == value
