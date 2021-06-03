#!/usr/bin/python3
"""
Function that returns True if the object is exactly an instance
of the specified class, otherwise is False
"""


def is_same_class(obj, a_class):
    """return object"""
    return type(obj) == a_class
