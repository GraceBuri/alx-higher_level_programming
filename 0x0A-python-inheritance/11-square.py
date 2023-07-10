#!/usr/bin/python3
"""import rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square class"""
    def __init__(self, size):
        """initialize square sizes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
