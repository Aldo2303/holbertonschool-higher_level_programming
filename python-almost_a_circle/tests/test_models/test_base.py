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

    def test_json_string_dictionary(self):
        list_dict = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        self.assertEqual(Base.to_json_string(list_dict),
                         '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        
        list_dict = []
        self.assertEqual(Base.to_json_string(list_dict), "[]")

        list_dict = None
        self.assertEqual(Base.to_json_string(list_dict), "[]")
        


if __name__ == '__main__':
    unittest.main()