#!/usr/bin/python3
""" Square Module """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Initializes the Square class

    Args:
        Rectangle: The parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes with arguments

        Args:
            size(int): size of the square
            x(int): the value of x of the square, Default to 0
            y(int): the value of y of the square, Default to 0
            id(int): the id of the sqaure instance, default to None
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns the string representation of the sqaure """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.size))

    @property
    def size(self):
        """ return the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets value to the size of the sqaure

        Args:
            value(int): the value to assign to size
        """
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """ replaces values with the arguments to all attribute

        Args:
            args: arguments of the function
            kwargs: if args not available, use dictionary values to replace
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for ky, vl in kwargs.items():
                if ky == 'id':
                    self.id = vl
                elif ky == 'size':
                    self.size = vl
                elif ky == 'x':
                    self.x = vl
                elif ky == 'y':
                    self.y = vl

    def to_dictionary(self):
        """ returns dictionary representation of the sqquare """
        dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dict
