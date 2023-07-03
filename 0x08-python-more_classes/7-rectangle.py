#!/usr/bin/python3
""" Defines a new class Rectangle """


class Rectangle():
    """ Initializes a new rectanlge """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Calculates and returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculates and returns the perimeter of the rectangle """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Prints print_symbol depending on the width and height """
        matrix = ''
        if (self.__width == 0 or self.__height == 0):
            return ("")
        else:
            for row in range(self.__height):
                for col in range(self.__width):
                    try:
                        matrix += str(self.print_symbol)
                    except Exception:
                        matrix += type(self).print_symbol
                if row < self.__height - 1:
                    matrix += '\n'
            return (matrix)

    def __repr__(self):
        """
        return a string representation of the
        rectangle to be able to recreate a new instance by using eval()
        """
        return ('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """
        Print Bye rectangle... when an instance of a rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
