#!/usr/bin/python3
""" Parent class Student """


class Student:
    """ public attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ public method to return the dictionary
    represetation of a Student """
    def to_json(self):
        return self.__dict__
