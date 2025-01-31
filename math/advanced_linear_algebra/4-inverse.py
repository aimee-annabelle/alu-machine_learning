#!/usr/bin/env python3
import numpy as np

def inverse(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is non-empty and square
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    try:
        # Convert to numpy array
        np_matrix = np.array(matrix, dtype=float)

        # Compute inverse
        inv_matrix = np.linalg.inv(np_matrix)

        # Convert result back to list of lists
        return inv_matrix.tolist()
    except np.linalg.LinAlgError:
        # If matrix is singular, return None
        return None
