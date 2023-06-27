#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """unittests for the functions in class Rectangle"""

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

    def test_Type_Arg(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2, 0, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, [2, 5], 0, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, {"k": 0}, 12)
        with self.assertRaises(TypeError):
            Rectangle((10, 7), 2, 0, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "hello", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, {0}, 12)

    def test_negative_and_Zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 0, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, -2, 0, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -4, 0, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -4, 12)


if __name__ == "__main__":
    unittest.main()
