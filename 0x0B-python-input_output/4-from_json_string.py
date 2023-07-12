#!/usr/bin/python3
""" import json module """
import json


def from_json_string(my_str):
    """
    A function that returns a string representation of a json file
    """
    st = json.loads(my_str)
    return st
