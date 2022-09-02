#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of a string object."""
    with open(filename, mode="w", encoding="UTF-8") as f:
        return json.dump(my_obj, f)
