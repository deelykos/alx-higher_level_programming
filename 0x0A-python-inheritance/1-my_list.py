#!/usr/bin/python3
"""defines inherited list class, called Mylist"""


class MyList(list):
    """Implements sorted printing of the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
