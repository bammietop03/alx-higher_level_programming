#!/usr/bin/python3
"""Writes a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n"""
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
