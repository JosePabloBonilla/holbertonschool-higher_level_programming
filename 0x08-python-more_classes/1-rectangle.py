#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle():
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize values width and height"""
        self.width = width
        self.height = height

    @property
    """width"""
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """height"""
    def height(self):
        return (self.__height)

    @height.setter
    """height setter"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
