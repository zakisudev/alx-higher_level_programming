#!/usr/bin/python3
""" get user commit and name from github """

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    passwrd = sys.argv[2]
    res = requests.get(url, auth=HTTPBasicAuth(user, passwrd))
    print(res.json().get('id'))
