#!/usr/bin/python3
""" import json module"""
import json


""" A function that returns a json representation of an object """


def to_json_string(my_obj):
    js = json.dumps(my_obj)
    return js
