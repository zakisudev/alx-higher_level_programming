#!/usr/bin/python3
""" Fetching a url to print response """
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {type(response_body)}")
        print(f"\t- content: {response_body}")
        print(f"\t- utfcontent: {utf8_content}")
