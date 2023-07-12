#!/usr/bin/python3
""" A function to read a file  """


def read_file(filename=""):
    """ takes an input filename and prints to stdout  """

    with open(filename, mode='r', encoding="UTF-8") as f:
        print(f.read(), end="")
