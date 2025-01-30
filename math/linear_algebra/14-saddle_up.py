#!/usr/bin/env python3
"""
Module for performing matrix multiplication
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication of two matrices

    Parameters:
        mat1 (numpy.ndarray): First input matrix
        mat2 (numpy.ndarray): Second input matrix

    Returns:
        numpy.ndarray: Result of matrix multiplication
    """
    return np.matmul(mat1, mat2)
