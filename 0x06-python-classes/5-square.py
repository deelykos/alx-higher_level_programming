#!/usr/bin/python3
""" Defines a class square """


class Square:
    """ This represents a square """
    def __init__(self, size=0):
        """Instantiate a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """ Get the current size of square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the current size of square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method that returns current Square area """
        return self.__size ** 2

    def my_print(self):
        """ method that prints to stdout the square with
        character #
        """
        if self.__size == 0:
            print("")

        for row in range(0, self.__size):
            for column in range(0, self.__size):
                print("#", end="\n" if column == self.__size - 1 else "")
