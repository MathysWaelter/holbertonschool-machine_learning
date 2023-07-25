#!/usr/bin/env python3

"""Get the shape of a matrix. This is a list of the number of rows"""


def matrix_shape(matrix):
    """
    @matrix - The matrix to get the shape of.
    It can be a list of lists or a single list.
    @The shape of the matrix as a list of integers.
    If matrix is a list it is returned as a list
    """
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
