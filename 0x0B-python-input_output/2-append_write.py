#!/usr/bin/python3
""" A function to append a text file and returns the chars written """


def append_write(filename="", text=""):
    """ takes an input filename and appends a text file
    and returns the number of chars written """

    with open(filename, mode='a', encoding="UTF-8") as f:
        return f.write(text)
