#!/usr/bin/python3
"""Defines division of a metrix"""


def matrix_divided(matrix, div):
    """Function divides elements of a matrix"""
    if not all(
            isinstance(row, list) and
            all(isinstance(elem, (int, float)) for elem in row)
            for row in matrix
    ):
        raise TypeError("matrix must be a matrix of integers/floats")
    """Check if each row has the same size"""
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    """Check if div is a number and not equal to zero"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
