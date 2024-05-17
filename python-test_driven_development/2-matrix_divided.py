#!/usr/bin/python3
"""
This is the matrix_divided module.

This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix where each element has been divided by div.

    Args:
        matrix (list): list of lists of integers or floats.
        div (int, float): the divider, >= 0.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(nb / div, 2) for nb in row] for row in matrix]
