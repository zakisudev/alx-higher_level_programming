#!/usr/bin/python3

" Define a class Square "


class Square:
    " Represent a square instance "

    def __init__(self, size=0):
        """ Initialize the new square
        Args:
            size (int): The size of the new square
            """
        if not isintance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        " Calculates and returns the area of the new square "
        return (self.__size * self.__size)
