#!/usr/bin/python3
""" A function to read a file  """


def read_file(filename=""):
    with open("filename", encoding="UTF-8") as file:
        file.read()
