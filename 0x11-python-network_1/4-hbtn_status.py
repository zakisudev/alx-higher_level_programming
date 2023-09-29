#!/usr/bin/python3
""" send request and display the X-Request-Id value """
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.rgv[1])
    print(res.headers.get('X-Request-Id'))
