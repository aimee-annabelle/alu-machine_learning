#!/usr/bin/env python3
"""
Module for adding two matrices of similar dimensions
"""


def matrix_shape(matrix):
    """Helper function to get shape of a matrix"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape


def add_matrices(mat1, mat2):
    """
    Adds two matrices of the same shape

    Parameters:
        mat1: First matrix (list of lists)
        mat2: Second matrix (list of lists)

    Returns:
        New matrix containing sum of the matrices, or None if shapes differ
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    # Base case: if not list, return sum
    if not isinstance(mat1, list):
        return mat1 + mat2

    # Recursive case: map addition to each element
    return [add_matrices(m1, m2) for m1, m2 in zip(mat1, mat2)]
