#!/usr/bin/env python3

def inverse(matrix):
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is non-empty and square
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    # Get the size of the matrix
    n = len(matrix)

    # Create an identity matrix of the same size as the input matrix
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Function to perform matrix multiplication
    def multiply(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
                for i in range(n)]

    # Function to perform matrix transpose
    def transpose(matrix):
        return [[matrix[j][i] for j in range(n)] for i in range(n)]

    # Function to calculate the determinant of a matrix using recursion
    def determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for c in range(len(matrix)):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * determinant(minor)
        return det

    # Function to calculate the cofactor matrix
    def cofactor(matrix):
        cofactors = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
                row.append(((-1) ** (i + j)) * determinant(minor))
            cofactors.append(row)
        return cofactors

    # Calculate the determinant of the matrix
    det = determinant(matrix)

    # If determinant is 0, the matrix is singular (non-invertible)
    if det == 0:
        return None

    # Get the cofactor matrix and transpose it to get the adjugate matrix
    cofactors = cofactor(matrix)
    adjugate = transpose(cofactors)

    # Calculate the inverse by dividing the adjugate matrix by the determinant
    inverse_matrix = [[adjugate[i][j] / det for j in range(n)] for i in range(n)]

    return inverse_matrix
