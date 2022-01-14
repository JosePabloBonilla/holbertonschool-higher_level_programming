#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":

    urlPort = argv[1]
    response = Request(urlPort)

    try:
        with urlopen(response) as File:
            print(File.read().decode('utf-8'))

    except HTTPError as err:
        print('Error code: {}'.format(err.code))
