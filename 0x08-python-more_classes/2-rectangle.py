#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle():
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """width"""
    @property
    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """height"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """rectangle area"""
    def area(self):
        return (self.__height * self.__height)

    """rectangle perimeter"""
    def perimeter(self):
        if self.width == 0:
            return (0)
        if self.height == 0:
            return (0)
        return (2 * (self.__height + self.__width))
