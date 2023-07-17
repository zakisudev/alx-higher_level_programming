#!/usr/bin/python3
""" a Square class that inherits from Rectangle class """

from .rectangle import Rectangle


class Square(Rectangle):

    """ Initializes the Square class """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size 
        super().__init__(size, size, x, y, id)

    """ String presentation of the result """
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.size))

    """ return value for size """
    @property
    def size(self):
        return self.__size
    """ setting value for size """
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        self.__size = value

    """ updating arguments to attributes """
    def update(self, *args, **kwargs):
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

    """ Dictionary representation of the Square class """
    def to_dictionary(self):
        dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dict
