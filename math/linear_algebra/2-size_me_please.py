#!/usr/bin/env python3

"""
This module provides functions for calculating matrix shapes.
"""


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape
