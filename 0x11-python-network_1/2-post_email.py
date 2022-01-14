#!/usr/bin/python3
"""takes email, sends a POST request to the passed URL"""
import urllib.request import Request, urlopen
import urllib.parse import urlencode
import sys


if __name__ == "__main__":

    values = {'email': sys.argv[2]}
    data = urlencode(values).encode('utf-8')
    response = Request(argv[1], data)

    with urlopen(response) as File:
        print(File.read().decode('utf-8'))
