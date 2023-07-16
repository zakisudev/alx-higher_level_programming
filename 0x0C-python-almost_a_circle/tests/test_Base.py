""" Unittest for Base class """

import unittest
from models.base import Base


class TestBase_class(unittest.TestCase):
    """ test cases for creating a Base class """

    """ creating instances with empty agrs """
    def test_create_instance(self):
        b1 = Base()
        b2 = Base()
        assertEqual(b1.id, b2.id - 1)

    """ creating instances with 'None' as an arg """
    def test_None_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        assertEqual(b1.id, b2.id - 1)

    """ creating instances with ids """
    def test_create_with_id(self):
        asserEqual(Base(47).id, 47)

    """ create ids after unique ids """
    def test_nb_after_unique(slef):
        b1 = Base()
        b2 = Base(47)
        b3 = Base()
        asserEqual(b1.id, b3.id)
