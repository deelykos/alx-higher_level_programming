#!/usr/bin/python3
"""To verify if an obj is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """To check for specific class with type"""
    if type(obj) == a_class:
        return True
    else:
        return False
