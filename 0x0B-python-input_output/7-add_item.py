#!/usr/bin/python3
""" Import argv to work with arguments """
from sys import argv


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    adding = "add_item.json"

    try:
        new_list = load_from_json(adding)
    except FileNotFoundError:
        new_list = []
    new_list.extend(argv[1:])
    save_to_json(new_list, adding)
