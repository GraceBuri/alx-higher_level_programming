#!/usr/bin/python3
"""define an empty rectangle class"""


class Rectangle:
    """representation of a triangle rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """intialize new rectangle

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return rcctangle representation"""

        if self.__width == 0 or self.__height == 0:
            return ""

        string = []
        for i in range(self.__height):
            [string.append("#") for j in range(self.__width)]
            if i != self.height - 1:
                string.append("\n")
        return "".join(string)

    def __repr__(self):
        """Return string rectangle representation"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Print a message for deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
