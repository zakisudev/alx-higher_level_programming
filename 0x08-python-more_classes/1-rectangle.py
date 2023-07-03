#!/usr/bin/python3
""" Defines a new class Rectangle """


class Rectangle():
    """ Initializes a new rectanlge """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Getter for height value """
        return (self.__height)

    @property
    def width(self):
        """ Getter for width value """
        return (self.__width)

    @height.setter
    def height(self, value):
        """ Checkes and set the height to value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """ Checks and sets the width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
