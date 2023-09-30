#!/usr/bin/python3
""" Fetching a url to print response """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')
    utf8 = utf8_content.replace('\r', '')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(utf8_content))
