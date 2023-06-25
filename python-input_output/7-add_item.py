#!/usr/bin/python3
"""Module 7-add_item"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_obj = load_from_json_file(filename)
except FileNotFoundError:
    existing_obj = []

save_to_json_file(existing_obj + argv[1:], filename)
