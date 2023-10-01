#!/usr/bin/python3
""" send a POST request with a letter as a parameter """

import requests
import sys

if __name__ == "__main__":
    let = "" if len(sys.argv) == 1 else sys.argv[1]
    pay = {"q": let}

    res = requests.post("http://0.0.0.0:5000/search_user", data=pay)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
