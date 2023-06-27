#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """unittests for the functions in class Base"""

    def test_int_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_empty_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_default_id(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)


if __name__ == "__main__":
    unittest.main()
