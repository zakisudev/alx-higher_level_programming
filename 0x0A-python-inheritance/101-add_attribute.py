#!/usr/bin/python
""" Defines a function to add attributes if possible """


def add_attribute(obj, attribute, value):

    """ checks if not possible """
    if not hasattr(obj, "__dict__") and not isinstance(obj, type):
       raise TypeError("can't add new attribute")

    """ sets the attribute value """
    setattr(obj, attribute, value)
