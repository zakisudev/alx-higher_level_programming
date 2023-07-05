#!/usr/bin/python3
"""Unittest for max_integer([])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ Test for normal input """

    def test_max_integer(self):
        self.assertEqual(max_integer([-80, 90, 20, 55]), 90)
    
    """ Test for the same value input """
    def test_same_input(self):
        self.assertEqual(max_integer([456, 456, 456]), 456)

    """ Test for floating number """
    def test_float_numbers(self):
        self.assertEqual(max_integer([66.5, 12.6, 45.1, 49]), 66.5)

    """ Test for negative numbers """
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-31, -300, -45, -56]), -31)

    """ Test for all 0(zero) input """
    def test_with_zero_as_input(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    """ Test for None as input """
    def test_None_as_input(self):
        self.assertEqual(max_integer([]), None)

    """ Test for large inputs """
    def test_large_input_list(self):
        self.assertEqual(max_integer([
            123, 456, 789, 124, 125, 126, 127, 128, 129, 321,
            999, 325, 326, 327, 328, 329, 453, 451, 461, 458,
            459, 761, 764, 648, 394, 974, 649, 444, 678, 949
            ]), 999)

    """ Test for string as input """
    def test_string_as_input(self):
        with self.assertRaises(TypeError):
            max_integer([6, '11'])

    """ Test for a tuple as input """
    def test_tuple_as_list(self):
        with self.assertRaises(TypeError):
            max_integer([12, (23, 34)])

    """ Test for dictionary as input """
    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 11, 'key2': 55})
