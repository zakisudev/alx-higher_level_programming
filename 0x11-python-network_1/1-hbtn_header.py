#!/usr/bin/python3
""" request a url and display the X-Request-Id variable in the response """
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
