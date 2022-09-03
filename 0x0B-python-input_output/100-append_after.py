#!/usr/bin/python3
"""function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Defines the append_after function."""
    text = ""
    with open(filename,"r+", encoding="UTF-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
        f.write(text)
