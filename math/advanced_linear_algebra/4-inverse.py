#!/usr/bin/env python3

def inverse(matrix):
    """
    Calculates the inverse of a square matrix.

    Parameters:
    matrix (list of list of numbers): A square matrix represented as a list of lists.

    Returns:
    list of list of numbers: The inverse of the matrix if it's non-singular, or None if the matrix is singular.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the matrix is empty or not square.
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is non-empty and square (same number of rows and columns)
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    # Get the size of the matrix (number of rows/columns)
    n = len(matrix)

    # Create an identity matrix of the same size as the input matrix
    # Identity matrix has 1s on the diagonal and 0s elsewhere
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Function to perform matrix multiplication
    # Multiplies two matrices A and B
    def multiply(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
                for i in range(n)]

    # Function to perform matrix transpose
    # Transposes the matrix by swapping rows with columns
    def transpose(matrix):
        return [[matrix[j][i] for j in range(n)] for i in range(n)]

    # Function to calculate the determinant of a matrix using recursion
    def determinant(matrix):
        # Base case: If the matrix is 1x1, the determinant is just the element itself
        if len(matrix) == 1:
            return matrix[0][0]
        # Base case: If the matrix is 2x2, use the formula ad - bc
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        # Recursive case: For larger matrices, use cofactor expansion along the first row
        det = 0
        for c in range(len(matrix)):
            # Create the minor matrix by removing the current row and column
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            # Apply cofactor expansion formula with alternating signs
            det += ((-1) ** c) * matrix[0][c] * determinant(minor)
        return det

    # Function to calculate the cofactor matrix
    def cofactor(matrix):
        cofactors = []
        # For each element in the matrix, calculate the cofactor
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                # Create the minor by removing the current row and column
                minor = [row[:j] + row[j+1:] 
                         for row in (matrix[:i] + matrix[i+1:])]
                # Apply the formula for the cofactor (determinant of minor with sign alternation)
                row.append(((-1) ** (i + j)) * determinant(minor))
            cofactors.append(row)
        return cofactors

    # Calculate the determinant of the matrix
    det = determinant(matrix)

    # If determinant is 0, the matrix is singular (non-invertible), so return None
    if det == 0:
        return None

    # Get the cofactor matrix and transpose it to get the adjugate matrix
    cofactors = cofactor(matrix)
    adjugate = transpose(cofactors)

    # Calculate the inverse matrix by dividing each element of the adjugate matrix by the determinant
    # This step uses the formula: inverse(A) = adj(A) / det(A)
    inverse_matrix = [[adjugate[i][j] / det for j in range(n)]
                      for i in range(n)]

    return inverse_matrix
