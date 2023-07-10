#!/usr/bin/python3
""" Defines inherets_from function  """


def inherits_from(obj, a_class):
    """ Returns if an object is an instance of inhereted
    class of specified class """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
