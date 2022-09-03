#!/usr/bin/python3
""" This module returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Defines a Pascal triangle of size n."""
    if n <= 0:
        return []

    Triangle = [[1]]
    while len(Triangle) != n:
        revtri = Triangle[-1]
        x = [1]
        for i in range(len(revtri) - 1):
            x.append(revtri[i] + revtri[i + 1])
        x.append(1)
        Triangle.append(x)
    return Triangle
