#!/usr/bin/python3
""" Defines a new class MyInt """


class MyInt(int):
    def __init__(self, val):
        """ Initilizes with val """
        self.val = val

    def __eq__(self, val):
        """ returns the opposite of equal """
        return self.val != val

    def __ne__(self, val):
        """ return the opposite of not equal """
        return self.val == val
