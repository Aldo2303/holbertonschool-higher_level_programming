#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """"unittests for the function def max_integer(list=[]):"""

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(max_integer([]))

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_positive_int_or_float(self):
        self.assertEqual(max_integer([3, 5, 2, 1, 4]), 5)
        self.assertEqual(max_integer([3.8, 5.7, 2.6, 1.5, 4.4]), 5.7)

    def test_negative_int_or_float(self):
        self.assertEqual(max_integer([-3, -5, -2, -1, -4]), -1)
        self.assertEqual(max_integer([-3.8, -5.7, -2.6, -1.5, -4.4]), -1.5)

    def test_mix_positive_and_negative_int_or_float(self):
        self.assertEqual(max_integer([3, -5, 2, -1, 4]), 4)
        self.assertEqual(max_integer([3.8, -5.7, -2.6, 1.5, -4.4]), 3.8)

    def test_duplicated_int_or_float(self):
        self.assertEqual(max_integer([5, -5, -5, 5]), 5)
        self.assertEqual(max_integer([-3.8, 3.8, -3.8, -3.8, -3.8]), 3.8)

    def test_list_of_lists(self):
        self.assertEqual(max_integer([[5, 8.4], [3.6, 2]]), [5, 8.4])

    def test_list_of_strings(self):
        self.assertEqual(max_integer("3475812"), '8')
        self.assertEqual(max_integer("mhfxr"), 'x')
        self.assertEqual(max_integer(['m', 'h', 'f', 'x', 'r']), 'x')
        self.assertEqual(max_integer(["mhfr", 'x']), 'x')

    def test_failures(self):
        self.assertRaises(TypeError, max_integer, {3, 5}, {2, 1, 4})
        self.assertRaises(TypeError, max_integer, {3, 5, 2, 1, 4})
        self.assertRaises(TypeError, max_integer, [-3, 5.8, "str", {1.5, -4.4}])

if __name__ == "__main__":
    unittest.main()
