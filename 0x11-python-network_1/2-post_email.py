#!/usr/bin/python3
""" send a POST request with url & email and displays the response """
from urllib import request, parse
import argv

if len(argv) > 2:
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
