#!/usr/bin/python3
"""Checks if the object is an instance of a class
that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Defines instance of a class inherited"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
