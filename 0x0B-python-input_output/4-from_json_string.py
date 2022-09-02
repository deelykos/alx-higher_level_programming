#!/usr/bin/python3
"""returns JSON representation of an object (string)"""
import json


def from_json_string(my_str):
    """
    Uses the dump() method of the json module to
    return the JSON representation of my_obj
    Args:
        my_obj (str): string to get JSON representation of
    """
    return json.loads(my_str)
