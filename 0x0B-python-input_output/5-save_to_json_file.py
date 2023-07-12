#!/usr/bin/python3
""" Import the json module """
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes to a text file using json representation
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
