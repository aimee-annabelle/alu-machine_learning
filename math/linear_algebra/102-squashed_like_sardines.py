#!/usr/bin/env python3
"""
Module for concatenating matrices along a specific axis
"""


def matrix_shape(matrix):
    """Helper function to get shape of a matrix"""
    shape = []
    m = matrix
    while isinstance(m, list):
        shape.append(len(m))
        if not m:
            break
        m = m[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis

    Parameters:
        mat1: First matrix
        mat2: Second matrix
        axis: Axis along which to concatenate (default=0)

    Returns:
        New concatenated matrix, or None if matrices cannot be concatenated
    """
    # Get shapes of both matrices
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)

    # Check if shapes allow concatenation
    if len(shape1) != len(shape2):
        return None

    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None

    # Handle 1D arrays
    if len(shape1) == 1:
        if axis == 0:
            return mat1 + mat2
        return None

    # Handle multi-dimensional arrays
    if axis >= len(shape1):
        return None

    if axis == 0:
        return mat1 + mat2

    return [cat_matrices(mat1[i], mat2[i], axis - 1) for i in range(len(mat1))]
