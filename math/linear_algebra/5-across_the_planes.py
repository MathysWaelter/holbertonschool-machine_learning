#!/usr/bin/env python3
"""adds two 2D matrices."""

matrix_shape = __import__('2-size_me_please').matrix_shape


def add_matrices2D(mat1, mat2):
    """
    @param mat1 - First matrix to add.
    @param mat2 - Second matrix to add. Must have the same shape as mat1.

    @return The result of the addition or None if there is a problem.
    """
    result = [[0, 0], [0, 0]]

    if mat1 is None:
        return None
    if mat2 is None:
        return None

    # Returns None if the shape of the two matrices are different.
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    # Add all elements of the matrix to result.
    for x in range(len(mat1)):
        # Add the sum of the matrix to result.
        for y in range(len(mat1[0])):
            result[x][y] = mat1[x][y] + mat2[x][y]
    return result
