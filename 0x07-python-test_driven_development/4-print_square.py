#!/usr/bin/python3
""" This module prints a square with character # """


def print_square(size):
    """ prints square with #

    Args:
        size (int): Size must be an integer

    Raises:
        TypeError:
            size must be an integer
        ValueError:
            size must be >= 0
            size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end='\n' if column == size - 1 else "")
