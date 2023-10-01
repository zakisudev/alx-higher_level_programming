#!/usr/bin/python3
""" send a request to url and display the response decoded with ut-8 """
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    request = Request(sys.argv[1])
    try:
        with urlopen(request) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except HTTPError as err:
        print('Error code:', err.code)
