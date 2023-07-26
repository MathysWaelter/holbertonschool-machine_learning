#!/usr/bin/env python3


"""Concatenate two 2D matrices along a given axis."""

matrix_shape = __import__('2-size_me_please').matrix_shape


def cat_matrices2D(mat1, mat2, axis=0):
    """
    @param mat1 - The first matrix to concatenate. Must be a 2D matrix.
    @param mat2 - The second matrix to concatenate. Must be a 2D matrix.
    @param axis - The axis along which to concatenate. Default is 0.

    @return The concatenation of mat1 and mat2 along the given axis
    or None if there is an error.
    """

    # Returns a new matrix with the same shape as the two matrices.
    if axis == 0:
        # Returns the shape of the first matrix
        if matrix_shape(mat1[0]) != matrix_shape(mat2[0]):
            return None

        new_matrix = mat1 + mat2
    elif axis == 1:
        # Return the length of the two matrices.
        if len(mat1) != len(mat2):
            return None

        new_matrix = [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None

    return new_matrix
