#!/usr/bin/python3
""" Defines a square function """


def print_square(size):
    """ Prints square with # charatcter """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size == 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
