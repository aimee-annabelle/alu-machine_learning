#!/usr/bin/env python3
"""
Module for performing element-wise operations on NumPy arrays
"""
import numpy as np


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.
    
    Parameters:
        mat1 (numpy.ndarray): First input array
        mat2 (numpy.ndarray): Second input array or scalar
    
    Returns:
        tuple: Contains (sum, difference, product, quotient) of the element-wise operations
    """
    # Addition - np.add performs element-wise addition
    addition = np.add(mat1, mat2)
    
    # Subtraction - np.subtract performs element-wise subtraction
    subtraction = np.subtract(mat1, mat2)
    
    # Multiplication - np.multiply performs element-wise multiplication
    multiplication = np.multiply(mat1, mat2)
    
    # Division - np.divide performs element-wise division
    division = np.divide(mat1, mat2)
    
    # Return tuple of results
    return (addition, subtraction, multiplication, division)
