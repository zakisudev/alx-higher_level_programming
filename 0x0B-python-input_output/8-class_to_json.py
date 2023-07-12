#!/usr/bin/python3
"""
Define a module to return a dictionary
description with simple data structure
"""


def class_to_json(obj):
    return obj.__dict__
