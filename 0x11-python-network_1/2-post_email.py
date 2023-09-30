#!/usr/bin/python3
""" send a POST request with url & email and displays the response """
from urllib import request, parse
import sys

if __name == "__main__" :
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
