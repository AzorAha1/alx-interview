#!/usr/bin/env python3
"""function called 2dmatrix"""


def rotate_2d_matrix(matrix):
    """_summary_
    Args:
        matrix (_type_): _description_
    """
    reversedmatrix = matrix[::-1]
    zipped = zip(*reversedmatrix)
    transform_matrix = [list(row) for row in zipped]
    for i in range(len(transform_matrix)):
        for j in range(len(transform_matrix[i])):
            matrix[i][j] = transform_matrix[i][j]
