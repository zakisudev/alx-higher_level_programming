#!/usr/bin/python3
""" Parent class Student """


class Student:

    """ initializes Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """ Check and represent in json """
        if (type(attrs) == list and all(type(e) == str for e in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):

        """ replace all attrs of the Student """
        for x, y in json.items():
            setattr(self, x, y)
