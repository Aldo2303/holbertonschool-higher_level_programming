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
        """check the representation of list to json"""
        list_dict = [{'id': 1, 'width': 10, 'height': 7, 'x': 2}]
        self.assertEqual(Base.to_json_string(list_dict),
                         '[{"id": 1, "width": 10, "height": 7, "x": 2}]')

        list_dict = []
        self.assertEqual(Base.to_json_string(list_dict), "[]")

        list_dict = None
        self.assertEqual(Base.to_json_string(list_dict), "[]")

    def test_from_json_string_to_list(self):
        """check the representation of json to list"""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        self.assertEqual(Base.from_json_string(json_str),
                         [{'id': 89, 'width': 10, 'height': 4}])


if __name__ == '__main__':
    unittest.main()
