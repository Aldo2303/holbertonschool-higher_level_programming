#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """unittests for the functions in class Rectangle"""

    def test_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_int(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

    def test_int(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

    def test_empty(self):
        r4 = Rectangle(None, None)
        self.assertEqual(r4.width, None)
        self.assertEqual(r4.height, None)


if __name__ == "__main__":
    unittest.main()
