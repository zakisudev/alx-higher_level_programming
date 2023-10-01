#!/usr/bin/python3
"""takes in a URL https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('utf-8'))
