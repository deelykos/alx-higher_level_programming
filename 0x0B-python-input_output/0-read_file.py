#!/usr/bin/python3
""" This is a function that reads a text file
(UTF8) and prints it to stdout."""


def read_file(filename=""):
    """ Reads and prints the content of a UTF8 text file to stdout"""
    with open(filename, mode='r', encoding="UTF-8") as f:
        print(f.read(), end="")
