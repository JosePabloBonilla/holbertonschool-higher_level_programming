#!/usr/bin/python3
"""
writes a string to a file
"""


def write_file(filename="", text =""):
    """writes string to a file"""
    with open(filename, 'w', encoding='utf-8') as fd:
        return (fd.write(text))
