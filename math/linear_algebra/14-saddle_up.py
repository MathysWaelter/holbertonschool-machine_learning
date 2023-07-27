#!/usr/bin/env python3

"""Multiplies two matrices, with different shape."""
import numpy as np


def np_matmul(mat1, mat2):
    """

    @param mat1 - The first matrix to multiply. Must be a 1 - D array.
    @param mat2 - The second matrix to multiply. Must be a 1 - D array.

    @return The result of the matrix multiplication.
    If the matrices are not square the result is a scalar.
    """
    return np.matmul(mat1, mat2)
