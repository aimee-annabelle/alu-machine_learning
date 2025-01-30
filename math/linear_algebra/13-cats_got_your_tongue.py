#!/usr/bin/env python3
"""
Module for concatenating matrices along a specific axis
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis

    Parameters:
        mat1 (numpy.ndarray): First input matrix
        mat2 (numpy.ndarray): Second input matrix
        axis (int): Axis along which to concatenate (default=0)

    Returns:
        numpy.ndarray: Concatenated matrix
    """
    return np.concatenate((mat1, mat2), axis=axis)
