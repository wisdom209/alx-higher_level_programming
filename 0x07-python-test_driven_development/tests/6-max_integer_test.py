#!/usr/bin/python3
"""unit test module to for max_integer function"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class

    Args:
        unittest (class): inherits from unittest
    """

    def test_max_integer(self):
        """correct test
        """
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(4, result)

    def test_two_max_integers(self):
        """correct test
        """
        result = max_integer([1, 4, 5, 3, 2, 5])
        self.assertEqual(5, result)

    def test_list_is_empty(self):
        """List is empty test
        """
        result = max_integer([])
        self.assertEqual(None, result)

    def test_list_param_contains_only_one_arg(self):
        """List has more than 1 param
        """
        self.assertRaises(TypeError,
                          max_integer, 1, "2")

    def test_list_param_contains_only_one_arg(self):
        """List has more than 1 param
        """
        self.assertRaises(TypeError,
                          max_integer, [1, 2], [3, 4])

    def test_not_supported(self):
        """List param not supported
        """
        self.assertRaisesRegex(TypeError, "object of type *", max_integer, 1)


if __name__ == '__main__':
    unittest.main()
