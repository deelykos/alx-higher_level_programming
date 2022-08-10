#!/usr/bin/python3
""" This module defines `add_integer`. """


def add_integer(a, b=98):
    """ adds a and b

    Args:
        a (int or float): parameter 1
        b (int or float): parameter 2

    Raises:
          TypeError: a and b must be integer

    Returns:
            int: sum of a and b
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
