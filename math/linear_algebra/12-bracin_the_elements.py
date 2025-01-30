#!/usr/bin/env python3
"""Performs element-wise operations on matrices"""


def np_elementwise(mat1, mat2):
    """Return tuple of element-wise operations without loops or conditionals"""
    return (mat1 + mat2,
            mat1 - mat2,
            mat1 * mat2,
            mat1 / mat2)
