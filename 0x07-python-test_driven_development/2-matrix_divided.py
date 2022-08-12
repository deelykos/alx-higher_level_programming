#!/usr/bin/python3
""" This module defines division of a matrix. """


def matrix_divided(matrix, div):
    """ Division of all elements of a matrix.

    Args:
        matrix (list): List of int/float.
        div (number): int/float.

    Raises:
        TypeError: matrix must be a matrix (list of lists)
        of integers/floats.

        TypeError: Each row of the matrix must have the same size.
        TypeError: div must be a number.
        ZeroDivisionError: division by zero.

    Returns:
        new matrix.
    """
    new_row, new_matrix = [], []

    if type(matrix) is not list or matrix == []:
        raise TypeError(
                "matrix must be a matrix (list of lists) of "
                " integers/floats"
            )

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                )
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                )

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = list(map(lambda x: round(x / div, 2), row))
        new_matrix.append(new_row)

    return (new_matrix)
