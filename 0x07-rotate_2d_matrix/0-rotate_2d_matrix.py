#!/usr/bin/python3
"""
module for rotating a 2D matrixi inplace
"""


def rotate_2d_matrix(matrix):
    new_matrix = matrix[:]
    ith_col = []
    for i in range(len(matrix)):
        ith_col = [ith_row[i] for ith_row in new_matrix]
        matrix[i] = ith_col[::-1]
