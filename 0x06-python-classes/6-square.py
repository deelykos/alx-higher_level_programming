#!/usr/bin/python3
""" Defines a class square """


class Square:
    """ This represents a square """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Get the current position of square """
        return self.__position

    @position.setter
    def position(self, value):
        """set the current position of the square """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Method that returns current Square area """
        return self.__size ** 2

    def my_print(self):
        """ method that prints to stdout the square with
        character #
        """
        if self.__size == 0:
            print("")

        for row in range(0, self.__position[1]):
            print("")

        for row in range(0, self.__size):
            for element in range(0, self.__position[0]):
                print(" ", end="")
            for column in range(0, self.__size):
                print("#", end="")
            print("")
