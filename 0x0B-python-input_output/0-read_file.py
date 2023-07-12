#!/usr/bin/python3
""" A function to read a file  """


def read_file(filename=""):
    with open("filename", 'r', encoding="UTF-8") as f:
        f.read()
