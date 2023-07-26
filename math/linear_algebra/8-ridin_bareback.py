#!/usr/bin/env python3

"""multiplie two 2D matrices."""


def mat_mul(mat1, mat2):
    """
    @param mat1 - First matrix to add.
    @param mat2 - Second matrix to add. Must have the same shape as mat1.

    @return The result of the multiplication or None if there is a problem.
    """

    if mat1 is None or mat2 is None:
        return None

    if len(mat1[0]) != len(mat2):
        return None

    # Create a new matrix with appropriate dimensions
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
