#!/usr/bin/python3
"""Test Rectangle class"""
import unittest
import unittest.mock
from contextlib import redirect_stdout
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
import json


class TestRectangle(unittest.TestCase):
    """test rectangle class"""

    def test_initialization(self):
        """test initialization"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, Base().id - 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, Base().id - 1)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_setter(self):
        """test setter"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        err = e.exception.args[0]
        self.assertEqual(err, "height must be an integer")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2)
            r.width = -10
        err = e.exception.args[0]
        self.assertEqual(err, "width must be > 0")

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
        err = e.exception.args[0]
        self.assertEqual(err, "x must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        err = e.exception.args[0]
        self.assertEqual(err, "y must be >= 0")

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 2)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test Rectangle display"""
        r = Rectangle(3, 2)
        fs = StringIO()
        with redirect_stdout(fs):
            r.display()
        self.assertEqual("###\n###\n", fs.getvalue())

        r1 = Rectangle(2, 3, 2, 2)
        fs = StringIO()
        with redirect_stdout(fs):
            r1.display()
        self.assertEqual(fs.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        r2 = Rectangle(3, 2, 1, 0)
        fs = StringIO()
        with redirect_stdout(fs):
            r2.display()
        self.assertEqual(fs.getvalue(), " ###\n ###\n")

    def test__str__(self):
        """Test String representation"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(
            r2.__str__(), f"[Rectangle] ({Base().id - 1}) 1/0 - 5/5")

    def test_update(self):
        """Testing shape update"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(
            r1.__str__(), f"[Rectangle] ({Base().id - 1}) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(
            r1.__str__(), f"[Rectangle] ({Base().id - 1}) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(
            r1.__str__(), f"[Rectangle] ({Base().id - 2}) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(
            r1.__str__(), f"[Rectangle] ({Base().id - 3}) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(
            r1.__str__(), f"[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(
            r1.__str__(), f"[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """test to dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {
                         'x': 1, 'y': 9, 'id': Base().id - 1,
                         'height': 2, 'width': 10})

    def test_to_json_string(self):
        """test to json string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(
            dictionary, {"x": 2, "width": 10, "id": Base().id - 1,
                         "height": 7, "y": 8})

    def test_save_to_file(self):
        """test save to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            my_list = json.loads(file.read())
            self.assertEqual(my_list, [{"y": 8, "x": 2,
                                        "id": int(f"{Base().id - 2}"),
                                        "width": 10, "height": 7},
                                       {"y": 0, "x": 0,
                                        "id": int(f"{Base().id - 2}"),
                                        "width": 2, "height": 4}])

    def test_from_json_string(self):
        """test from json string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {
                         'height': 7, 'width': 1, 'id': 7}])

    def test_create(self):
        """test returning an instance"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(
            r2.__str__(), f"[Rectangle] ({Base().id - 2}) 1/0 - 3/5")

    def test_load_from_file(self):
        """test loading json from file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual([x.__str__() for x in list_rectangles_output],
                         [f"[Rectangle] ({Base().id - 4}) 2/8 - 10/7",
                          f"[Rectangle] ({Base().id - 4}) 0/0 - 2/4"])

    def test_load_from_csv(self):
        """Test load from csv"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output[0].id, r1.id)
        self.assertEqual(list_rectangles_output[0].width, 10)
        self.assertEqual(list_rectangles_output[0].height, 7)
        self.assertEqual(list_rectangles_output[0].x, 2)

        self.assertEqual(list_rectangles_output[1].width, 2)
        self.assertEqual(list_rectangles_output[1].height, 4)
        self.assertEqual(list_rectangles_output[1].x, 0)

    def test_save_to_file_csv(self):
        pass
