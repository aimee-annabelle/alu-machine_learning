#!/usr/bin/env python3
"""
Module for concatenating matrices along a specific axis
"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    
    Parameters:
        mat1: First input matrix
        mat2: Second input matrix
        axis (int): Axis along which to concatenate (default=0)
    
    Returns:
        Concatenated matrix
    """
    return mat1.__add__(mat2)
