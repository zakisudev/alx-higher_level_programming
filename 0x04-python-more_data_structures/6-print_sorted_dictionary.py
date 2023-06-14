#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.items())
    for x, y in new:
        print("{}: {}".format(x, y))
