#!/usr/bin/python3
"""  Base Class """
import json
import os
from os import path
""" Import modules to work with """


class Base:
    """ Base class for Rectangle and Square

    Args:
        id(int): The id of the instacne Default to None
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """ static method to json convertor """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    """ Writing JSON string to list_objs file """
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None or list_objs == []:
            jsn = '[]'
        else:
            jsn = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            f.write(jsn)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.

        Args:
            json_string: string to convert to list
        """
        deSer = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            deSer = json.loads(json_string)
        return deSer

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes aready set.

        Args:
            dictionary: used like **kwargs
        """

        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        elif cls.__name__ == 'Square':
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ Fetches a list of instances """

        file_name = cls.__name__ + ".json"
        tmp = []
        list_dics = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                d = f.read()
                list_dics = cls.from_json_string(d)
                for i in list_dics:
                    tmp.append(cls.create(**i))
        return tmp

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialize and saves list_objs to csv format

        Args:
            list_objs: list of instances
        """

        if (type(list_objs) != list and list_objs is not None
                and all(isinstance(i, cls) for i in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        file_name = cls.__name__ + ".csv"
        dic = []
        with open(file_name, "w") as f:
            if list_objs is not None:
                for obj in list_objs:
                    dic.append(obj.to_dictionary())
            f.write(cls.to_json_string(dic))

    @classmethod
    def load_from_file_csv(cls):
        """ DeSerialize csv format from a file

        Returns: list of instances
        """

        file_name = cls.__name__ + ".csv"
        if path.exists(file_name):
            with open(file_name, "r") as f:
                objL = []
                csvL = Base.from_json_string(f.read())
                for obj in csvL:
                    objL.append(cls.create(**obj))
                return objL
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a Turtle window and draw rectanlges and squares

        Args:
            list_rectangles: list of Rectangle instances
            list_squares: list of Square instances
        """
        import turtle
        import time
        from random import randrange

        tr = turtle.Turtle()
        tr.color('beige')
        turtle.bgcolor('violet')
        tr.shape('square')
        tr.pensize(8)

        for i in (list_rectangles + list_squares):
            tr.penup()
            tr.setpos(0, 0)
            turtle.Screen().colormode(255)
            tr.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(tr, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """ Rectangle and Square drawing helper """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
