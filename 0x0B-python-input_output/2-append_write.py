#!/usr/bin/python3
"""
write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends string at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as fd:
        return(fd.write(text))
