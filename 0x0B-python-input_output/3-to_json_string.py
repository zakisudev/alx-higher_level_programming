#!/usr/bin/python3
""" import json module """
import json


def to_json_string(my_obj):
    """
    A function that returns a json representation of an object
    """
    js = json.dumps(my_obj)
    return js
