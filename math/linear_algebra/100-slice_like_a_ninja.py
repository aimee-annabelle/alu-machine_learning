#!/usr/bin/env python3
"""
Module for slicing matrices along specific axes
"""


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specified axes

    Parameters:
        matrix (numpy.ndarray): Input matrix to slice
        axes (dict): Dictionary where key is axis to slice along and value is
                    tuple representing the slice to make along that axis

    Returns:
        numpy.ndarray: Sliced matrix
    """
    slices = [slice(None)] * len(matrix.shape)
    for axis, slice_params in axes.items():
        slices[axis] = slice(*slice_params)
    return matrix[tuple(slices)]
