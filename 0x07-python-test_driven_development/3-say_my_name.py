#!/usr/bin/python3
""" This module prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>

    Args:
        first name (str): must be a string
        last name (str): must be a string

    Raises:
        TypeError:
            first_name must be a string or
            last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
