#!/usr/bin/python3
"""  Base Class """


class Base:
    __nb_objects = 0
    """  Initializes the class """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
