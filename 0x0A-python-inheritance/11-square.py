#!/usr/bin/python3
"""import rectangle subclass"""
Base = __import__('7-base_geometry').BaseGeometry


class Square(Base):
    """represents a square class"""
    def __init__(self, size):
        """initialize square sizes"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """print string rep of square"""
        return '[Square]' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """calculate square area"""
        return self.__size ** 2
