#!/usr/bin/python3
""" Defines a class BaseGeometry  """


class BaseGeometry:
    """ Defines an instance method area """

    def area(self):
        raise Exception("area() is not implemented")

    """ public instance method integer_validator """
    def integer_validator(self, name, value):

        """ Raise a typeerror if value is not an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        """ Raise a valueerror if value is less or equal to 0 """
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
