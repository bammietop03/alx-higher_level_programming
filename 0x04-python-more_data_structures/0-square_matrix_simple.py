#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            num = i ** 2
            new_row.append(num)
        temp_matrix.append(new_row)
    return temp_matrix
