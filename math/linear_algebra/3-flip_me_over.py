#!/usr/bin/env python3

"""This is a function to make it easy to transpose a matrix."""


def matrix_transpose(matrix):
    """
    @matrix - The matrix to transpose. Must be a list of lists.
    @return The transpose of the matrix.
    """
    rows = len(matrix)
    columns = len(matrix[0])

    transpose = []
    # Create a transpose of the matrix.
    for j in range(columns):
        row = []
        # Append the matrix to the row.
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)

    return transpose
