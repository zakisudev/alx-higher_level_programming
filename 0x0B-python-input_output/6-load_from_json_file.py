#!/usr/bin/python3
""" Import json to create an object from json """
import json


def load_from_json_file(filename):
    """ creates an object """
    with open(filename, mode="r") as f:
        return json.load(f)
