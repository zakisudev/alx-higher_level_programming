#!/usr/bin/python3
""" a functio add_attribute to add attribute """


def add_attribute(obj, attribute, value):
    """ Accepts three parameters (obj, attribute, value).
    Adds a new attribute to an object if it’s possible.
    """

    if not hasattr(obj, "__dict__") and not isinstance(obj, type):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
