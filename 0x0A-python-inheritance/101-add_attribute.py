#!/usr/bin/python
""" Defines a function to add attributes if possible """


def add_attribute(obj, att, value):

    """ checks if not possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    """ sets the attribute value """
    setattr(obj, att, value)
