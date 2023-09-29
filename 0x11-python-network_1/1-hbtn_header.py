#!/usr/bin/python3
""" request a url and display the X-Request-Id variable in the response """
import urllib.request
import sys

url = sys.argv[1]

if len(sys.argv) == 2:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
