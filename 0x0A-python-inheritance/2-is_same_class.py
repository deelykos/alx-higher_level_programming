#!/usr/bin/python3
"""To verify if an obj is an instance of a class"""

def is_same_class(obj, a_class):
    """Defines instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
