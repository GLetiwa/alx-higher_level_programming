#!/usr/bin/python3
"""Unittest for max integer"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_mixed_list(self):
        result = max_integer([1, 2.5, 4, 3])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result)

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -4, -2])
        self.assertEqual(result, -1)

    def test_duplicate_numbers(self):
        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
