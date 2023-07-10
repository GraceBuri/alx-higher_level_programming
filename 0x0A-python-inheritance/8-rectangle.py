#!/usr/bin/python3
"""import BaseGeometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('height', height)
        self.__height = height
        self.integer_validator('width', width)
        self.__width = width
