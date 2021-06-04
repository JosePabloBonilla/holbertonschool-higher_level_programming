#!/usr/bin/python3
"""
function that writes an object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """save object using JSON representation"""
    with open(filename, 'w') as fd:
        json.dump(my_obj, fd)
