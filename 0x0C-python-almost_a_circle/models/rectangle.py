#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the Rectangle class
        that inherits from Base class

        Args:
            width(int): width of the instance Rectangle
            height(int): height of the instance Rectangle
            x(int): x of the instance. Default to 0
            y(int): y of the instance. Default to 0
            id(int): id of the instance. Default to None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.y):
            print()

        for j in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for h in range(self.width):
                print("#", end="")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[4]
        else:
            for ky, vl in kwargs.items():
                if ky == 'id':
                    self.id = vl
                elif ky == 'width':
                    self.width = vl
                elif ky == 'height':
                    self.height = vl
                elif ky == 'x':
                    self.x = vl
                elif ky == 'y':
                    self.y = vl

    def to_dictionary(self):
        dict = {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
        return dict
