#!/usr/bin/python3
"""Test Square class"""
import unittest
import unittest.mock
from contextlib import redirect_stdout
from io import StringIO
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """test square class"""

    def test_initialization(self):
        """test initialization"""
        r1 = Square(5)
        self.assertEqual(r1.id, Base().id - 1)
        s2 = Square(2, 10)
        self.assertEqual(s2.id, Base().id - 1)
        s3 = Square(2, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_setter(self):
        """test setter"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(5)
            s1.size = "9"
        err = e.exception.args[0]
        self.assertEqual(err, "width must be an integer")

    def test_area(self):
        """Test area calculation"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_display(self):
        """Test Rectangle display"""
        r = Square(5)
        fs = StringIO()
        with redirect_stdout(fs):
            r.display()
        self.assertEqual("#####\n#####\n#####\n#####\n#####\n", fs.getvalue())

        s1 = Square(2, 2)
        fs = StringIO()
        with redirect_stdout(fs):
            s1.display()
        self.assertEqual(fs.getvalue(), "  ##\n  ##\n")

        s1 = Square(3, 1, 3)
        fs = StringIO()
        with redirect_stdout(fs):
            s1.display()
        self.assertEqual(fs.getvalue(), "\n\n\n ###\n ###\n ###\n")

    def test__str__(self):
        """Test String representation"""
        s1 = Square(5)
        self.assertEqual(s1.__str__(), f"[Square] ({Base().id - 1}) 0/0 - 5")

    def test_update(self):
        """Testing shape update"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(
            s1.__str__(), f"[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(
            s1.__str__(), f"[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(
            s1.__str__(), f"[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(
            s1.__str__(), f"[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(
            s1.__str__(), f"[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(
            s1.__str__(), f"[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(
            s1.__str__(), f"[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """test to dictionary"""
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {
                         'id': Base().id - 1, 'x': 2, 'size': 10, 'y': 1})
