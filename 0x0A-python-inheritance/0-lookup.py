#!/usr/bin/python3
"""
function that returns a list of available attributes and method of an object
"""


def lookup(obj):
    """return the list of attributes and methods available"""
    return dir(obj)
