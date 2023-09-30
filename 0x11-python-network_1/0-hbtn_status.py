#!/usr/bin/python3
""" Fetching a url to print response """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utfcontent:", utf_content)
