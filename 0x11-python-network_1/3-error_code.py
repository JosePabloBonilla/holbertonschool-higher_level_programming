#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
import urllib.request
import sys
from urllib.error import HTTPError


if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.rquest.urlopen(req) as response:
            html = response.read()
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        print(html.decode('utf-8))
