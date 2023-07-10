#!/usr/bin/python3
""" Defines a new class MyInt """


class MyInt(int):
    """ Initializes with value """

    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        """ returns the opposite of equal """
        return self.value != value

    def __ne__(self, value):
        """ return the opposite of not equal """
        return self.value == value
