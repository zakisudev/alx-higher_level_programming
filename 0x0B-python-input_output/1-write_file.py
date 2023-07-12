#!/usr/bin/python3
""" A function to write a text file and returns tje chars written """


def write_file(filename="", text=""):
    """ takes an input filename and writes a text file
    and returns the number of chars written """

    with open(filename, mode='w', encoding="UTF-8") as f:
        return f.write(text)
