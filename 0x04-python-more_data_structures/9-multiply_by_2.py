#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for x, y in a_dictionary:
        new = {}
        new.append(x, y ** 2)
    return new
