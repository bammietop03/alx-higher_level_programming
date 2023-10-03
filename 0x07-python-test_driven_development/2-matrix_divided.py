#!/usr/bin/python3
"""
    a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
                   Each row of the matrix must have the same size

        ZeroDivisionError: If div is equal to 0.
    """

    if (not isinstance(matrix, list) or matrix == [] or not
        all(isinstance(row, list)
            for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)

    return result_matrix
