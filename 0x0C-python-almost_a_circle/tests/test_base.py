""" Unittest for Base class """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_class(unittest.TestCase):
    """ test cases for creating a Base class """

    """ creating instances with empty agrs """
    def test_create_instance(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    """ creating instances with 'None' as an arg """
    def test_None_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    """ creating instances with ids """
    def test_create_with_id(self):
        self.assertEqual(Base(47).id, 47)

    """ create ids after unique ids """
    def test_nb_after_unique(self):
        b1 = Base()
        b2 = Base(4)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    """ test for rectangle type """
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
    """ test for two rectangle dictionaries """
    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
    """ test for square type """
    def test_to_json_string_square_type(self):
        s = Square(4, 7, 9, 6)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
    """ test for two square dictionaries """
    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)
    """ test for empty list """
    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))
    """ test for None condition """
    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))
    """ test for no args """
    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
    """ test for more than max args """
    def test_to_json_string_more_than_max_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """ Unittests for testing save_to_file method of Base class """

    @classmethod
    def tearDown(self):
        """ remove created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass
    """ test for two rectangles """
    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)
    """ test for two squares """
    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)
    """ test for file name """
    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
    """ test for file overwrite """
    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
    """ test for None condition """
    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
    """ test for empty list """
    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
    """ test for no args """
    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
    """ test for more than max args """
    def test_save_to_file_more_than_max_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    """ test for two rectangles """
    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
    """ test for two squares """
    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 47, "size": 8, "height": 9},
            {"id": 74, "size": 5, "height": 6}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
    """ test for string None """
    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))
    """ test for empty list """
    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))
    """ test for no args """
    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()
    """ test for more than max arg """
    def test_from_json_string_more_than_max_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """ Unittests for testing create method of Base class """

    """ test for creating rectangle """
    def test_create_rectangle_new(self):
        rec1 = Rectangle(4, 7, 8, 9, 6)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (6) 8/9 - 4/7", str(rec2))
    """ test for rectangle equality """
    def test_create_rectangle_equals(self):
        rec1 = Rectangle(4, 7, 8, 9, 6)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertNotEqual(rec1, rec2)
    """ test for creating square """
    def test_create_square_new(self):
        sq1 = Square(4, 7, 9, 6)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (6) 7/9 - 4", str(sq2))
    """ test for square equality """
    def test_create_square_equals(self):
        sq1 = Square(4, 7, 9, 6)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)


class TestBase_load_from_file(unittest.TestCase):
    """ Unittests for testing load_from_file_method of Base class """

    @classmethod
    def tearDown(self):
        """ remove created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
    """ test for rectangle types """
    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
    """ test for square types """
    def test_load_from_file_square_types(self):
        s1 = Square(4, 7, 9, 6)
        s2 = Square(4, 1, 3, 6)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))
    """ test for no file """
    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)
    """ test for more than max args """
    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """ Unittests for testing save_to_file_csv method of Base class """

    @classmethod
    def tearDown(self):
        """ remove created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass
    """ test for two rectangles """
    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())
    """ test for two squares """
    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())
    """ test for class name """
    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())
    """ test for csv overwrite """
    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())
    """ test for None csv """
    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())
    """ test for empty list """
    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())
    """ test fpr no args """
    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
    """ test for more than max args """
    def test_save_to_file_csv_more_than_max_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """ Unittests for testing load_from_file_csv method from Base class """

    @classmethod
    def tearDown(self):
        """ Remove created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
    """ test for csv rectangle types """
    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(4, 7, 8, 9, 6)
        r2 = Rectangle(4, 1, 2, 3, 6)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
    """ test for csv square types """
    def test_load_from_file_csv_square_types(self):
        s1 = Square(4, 7, 9, 6)
        s2 = Square(4, 1, 3, 6)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))
    """ test for no file """
    def test_load_from_file_csv_with_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)
    """ test for more than max """
    def test_load_from_file_csv_more_than_max_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
