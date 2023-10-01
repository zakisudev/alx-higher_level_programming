#!/usr/bin/python3
""" send request and display the X-Request-Id inside the response """

import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
