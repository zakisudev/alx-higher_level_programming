""" Import modules for test cases for Rectanlge subclass """
import unittest
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ test cases for Rectangle subclass instantiation """

    """ test for instance case """
    def test_base_instance(self):
        self.assertIsInstance(Rectangle(4, 7), Base)
    """ test for no agruments input """
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
    """ test for single arg input """
    def test_single_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4)
    """ test for minimum amount of args input """
    def test_min_args(self):
        rec1 = Rectangle(4, 7)
        rec2 = Rectangle(7, 4)
        self.assertEqual(rec1.width, rec2.height)
    """ test for maximum amount of args input """
    def test_max_args(self):
        self.assertEqual(6, Rectangle(4, 7, 8, 9, 6).id)
    """ test for more than the max arg input """
    def test_more_than_max_args(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 7, 8, 9, 6, 5)
    """ test for getting width """
    def test_getting_width(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        self.assertEqual(4, rec.width)
    """ test for getting height """
    def test_getting_height(slef):
        rec = Rectangle(4, 7, 8, 9, 6)
        self.asssertEqual(7, rec.height)
    """ test for setting width """
    def test_setting_width(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        rec.width = 5
        self.assertEqual(5, rec.width)
    """ test for setting height """
    def test_setting_height(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        rec.height = 5
        self.assertEqual(5, rec.height)
    """ test for getting x """
    def test_getting_x(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        self.assertEqual(8, rec.x)
    """ test for getting y """
    def test_getting_y(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        self.assertEqual(9, rec.y)
    """ test for setting x """
    def test_setting_x(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        rec.x = 5
        self.assertEqual(5, rec.x)
    """ test for setting y """
    def test_setting_y(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        rec.y = 5
        self.assertEqual(5, rec.y)
    """ accessing private variable width """
    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 7, 8, 9, 6).__width)
    """ accessing private variable height """
    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 7, 8, 9, 6).__height)
    """ accessing private variable x """
    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 7, 8, 9, 6).__x)
    """ accessing private variable y """
    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 7, 8, 9, 6).__y)

class TestWidthAndHeight(unittest.TestCase):
    """ Test case for width and height vars """

    """ test for float input width """
    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(4.7, 8)
    """ test for float input height """
    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 7.8)
    """ test for string input width """
    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("4", 7)
    """ test for string input hegiht """
    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "7")
    """ test for list input width """
    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4, 7], 8)
    """ test for list input height """
    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [7, 8])
    """ test for set input width """
    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 7}, 8)
    """ test for set input height """
    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {7, 8})
    """ test for negative value for width """
    def test_width_neg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 7)
    """ test for negative value for height """
    def test_height_neg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -7)
    """ test for zero(0) value input for width """
    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)
    """ test for zero(0) value input for height """
    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)

class TestxAndy(unittest.TestCase):

    """ test for float input x """
    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 7, 8.9, 6)
    """ test for float input y """
    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 7, 8, 9.6)
    """ test for string input x """
    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 7, '8')
    """ test for string input y """
    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 7, 8, 9.6)
    """ test for list input x """
    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 7, [8, 9])
    """ test for list input y """
    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 7, 8, [9, 6])
    """ test for set input x """
    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 7, {8, 9})
    """ test for set input y """
    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 7, 8, {9, 6})
    """ test for negative value for x """
    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            Rectangle(4, 7, -8)
    """ test for negative value for y """
    def test_y_neg(self):
        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            Rectangle(4, 7, 8, -9)
    """ test for zero(0) value input for x """
    def test_x_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            Rectangle(4, 7, 0)
    """ test for zero(0) value input for y """
    def test_y_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            Rectangle(4, 7, 8, 0)

class TestRecArea(unittest.TestCase):
    """ test cases for Area input """

    """ regular integer input for width and height """
    def test_reg_width_height(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        self.assertEqual(28, rec.area())
    """ test for area after changed value """
    def test_value_changed(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        rec.width = 5
        rec.height = 2
        self.assertEqual(10, rec.area())
    """ test for area single arg input """
    def test_single_area_arg(self):
        rec = Rectangle(4, 7, 8, 9, 6)
        with self.assertRaises(TypeError):
            r.area(5)
