#!/usr/bin/python3
""" This module prints a tecxt with two lines after each
    of these characters: . ? and :
"""


def text_indentation(text):
    """ Defines text indentation

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
