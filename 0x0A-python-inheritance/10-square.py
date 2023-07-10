#!/usr/bin/python3
""" Import the Basegeometry module """

Rectangle = __import__('9-rectangle').Rectangle

""" A derived class that inherits from Basegeometry class """


class Square(Rectangle):

    """ inistantiates with size """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
