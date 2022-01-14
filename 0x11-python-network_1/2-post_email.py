#!/usr/bin/python3
"""takes email, sends a POST request to the passed URL"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = urlencode(url).encode('utf-8')
    req = Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('utf-8'))
