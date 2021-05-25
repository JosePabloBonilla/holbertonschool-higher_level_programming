#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle():
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize values width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
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
    def height(self):
        """height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """rectangle perimeter"""
        if self.width == 0:
            return (0)
        if self.height == 0:
            return (0)
        return (2 * (self.__height + self.__width))
