#!/usr/bin/env python3

"""
This module provides functions for matrix operations.

Currently, it includes a function to transpose a matrix.
"""


def matrix_transpose(matrix):
    """
    Transpose a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list representing the transposed matrix.
    """
    transpose = [[0 for _ in range(len(matrix))]
                 for _ in range(len(matrix[0]))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            transpose[j][i] = matrix[i][j]
    return transpose
