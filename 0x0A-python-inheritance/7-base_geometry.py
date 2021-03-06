#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry():
    """Base Geometry"""

    def area(self):
        """raise exception error with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
