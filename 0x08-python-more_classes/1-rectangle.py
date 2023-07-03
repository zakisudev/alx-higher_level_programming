#!/usr/bin/python3
""" Defines a new class Rectangle """


class Rectangle():
    """ Initializes a new rectanlge """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Gets the height value """
    @property
    def height(self):
        return (self.__height)

    """ Gets the width value """
    @property
    def width(self):
        return (self.__width)

    """ Checks and sets the height value """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    """ Checks and sets the width value """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
