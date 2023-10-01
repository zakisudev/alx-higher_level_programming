#!/usr/bin/python3
"""takes in a URL https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        utf = html.decode('utf-8')
        utf8 = utf.replace('\r', '')
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(utf8))
