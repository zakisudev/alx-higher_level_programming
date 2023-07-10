#!/usr/bin/python3
""" Defines a function is_same_class """


def is_same_class(obj, a_class):
    """ Returns true if the obj is an instance of a_class """

    return type(obj) is a_class
