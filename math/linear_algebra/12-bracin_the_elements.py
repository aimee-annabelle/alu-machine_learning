#!/usr/bin/env python3
"""
Module for performing element-wise operations on arrays
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.
    
    Parameters:
        mat1: First input array
        mat2: Second input array or scalar
    
    Returns:
        tuple: Contains (sum, difference, product, quotient) of the element-wise operations
    """
    # If mat2 is a scalar, convert it to a matrix of the same shape as mat1
    if isinstance(mat2, (int, float)):
        mat2 = [[mat2 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    
    # Element-wise addition
    addition = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] 
                for i in range(len(mat1))]
    
    # Element-wise subtraction
    subtraction = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] 
                   for i in range(len(mat1))]
    
    # Element-wise multiplication
    multiplication = [[mat1[i][j] * mat2[i][j] for j in range(len(mat1[0]))] 
                      for i in range(len(mat1))]
    
    # Element-wise division
    division = [[mat1[i][j] / mat2[i][j] for j in range(len(mat1[0]))] 
                for i in range(len(mat1))]
    
    return (addition, subtraction, multiplication, division)
