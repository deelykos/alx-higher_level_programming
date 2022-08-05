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

    def __eq__(self, other):
        """ Define the == comparism to a square. """
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
