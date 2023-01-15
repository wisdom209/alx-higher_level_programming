#!/usr/bin/python3
"""Test Rectangle class"""
import unittest
import unittest.mock
from contextlib import redirect_stdout
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


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
