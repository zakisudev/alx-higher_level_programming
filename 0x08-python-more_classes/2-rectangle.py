class Rectangle():
    """ Defines a new rectangle """


    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Getter for height value """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Getter for width value """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Calculates and returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculates and returns the perimeter of the rectangle """
        return (self.__width * 2 + self.__height * 2)
