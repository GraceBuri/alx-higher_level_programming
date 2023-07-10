#!/usr/bin/python3
"""import BaseGeometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator('height', height)
        self.__height = height
        super().integer_validator('width', width)
        self.__width = width

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
