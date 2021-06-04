#!/usr/bin/python3
"""
functions that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """reads file"""
    with open(filename, encoding="utf-8") as fd:
        print(fd.read(), end="")
