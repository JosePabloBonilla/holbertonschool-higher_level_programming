#!/usr/bin/python3
"""
New class square
"""


class Square():
    """ Defines a square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Define area of square """
        return (self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
