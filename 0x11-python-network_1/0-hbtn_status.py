#!/usr/bin/python3
""" Fetching a url to print response """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    response_body = response.read()
    utf8_content = response_body.decode('utf-8')

print("Body response:")
print(f"    - type: {type(response_body)}")
print(f"    - content: {response_body}")
print(f"    - utfcontent: {utf8_content}")
