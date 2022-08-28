#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    # if in task 9 I used str.(self.__class__.__name__) instead of the class
    # name, I won't have added this method. Because my super() would cover
    # for it.
