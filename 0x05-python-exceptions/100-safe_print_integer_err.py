#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return False
    else:
        return True
