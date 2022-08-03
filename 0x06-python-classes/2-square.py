#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Instantiation of size attribute as private with optional """
    def __init__(self, size=0):
        self.__size = size

        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
