#!/usr/bin/python3
""" Defines Mylist class """


class MyList(list):
    """ Initializes Mylist class """

    def print_sorted(self):
        """ defines a function print_sorted """
        print(sorted(self))
