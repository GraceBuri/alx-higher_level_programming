#!/usr/bin/python3

class Square:
    """Represent a square"""

    def_init_(self, size):
        """initialize new square


        Args:
        size(int): The size of the new square
    """
    self._size = size

    def area(self):
        """Calculate and return area of square"""
        return self.self._size ** 2
