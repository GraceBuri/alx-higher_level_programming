#!/usr/bin/python3
"""defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """represents base geometry"""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer value passed"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
