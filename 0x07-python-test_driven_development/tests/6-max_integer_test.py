#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_mixed_numbers(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -4, -2])
        self.assertEqual(result, -1)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
