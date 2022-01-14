#!/usr/bin/python3
"""takes email, sends a POST request to the passed URL"""
import urllib.request
import urllib.parse
import sys


web = sys.argv[1]
mail = urllib.parse.urlencode({'email': sys.argv[2]})
mail = mail.encode('utf8')
with urllib.request.urlopen(web, mail) as response:
    print(response.read().decode('utf8'))
