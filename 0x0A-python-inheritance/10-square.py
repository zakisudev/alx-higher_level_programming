#!/usr/bin/python3
""" Import the Basegeometry module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


""" A base class that inherits from Basegeometry class """


class Rectangle(BaseGeometry):

    """ instaniates width and height and
    validates using Parent class method """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """ area method implementation """
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
class Square(Rectangle):

    """ inistantiates with size """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """ Implements the area calculation of a square with (size*size) """
    def area(self):
        return self.__size * self.__size
