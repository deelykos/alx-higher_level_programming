#!/usr/bin/python3
""" This module creates a Rectangle """


class Rectangle:
    """Defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initiation of Rectangle
        Args:
            width (int): Width must be an integer
            height (int): height must be an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/set the current height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Return the printable representation of a Rectangle
        with # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rect_str += '#'
            if h != self.__height - 1:
                rect_str += '\n'
        return rect_str
