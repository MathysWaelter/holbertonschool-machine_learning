#!/usr/bin/env python3


"""Elementwise multiplication of two NxM matrices"""


def np_elementwise(mat1, mat2):
    """
    @param mat1 - First matrix to be operated on
    @param mat2 - Second matrix to be operated on

    @return result of operation
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
