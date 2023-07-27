#!/usr/bin/env python3

"""Concatenate two arrays along a given axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    @param mat1 - Array to concatenate. Must be at least 2D.
    @param mat2 - Array to concatenate. Must be at least 2D.
    @param axis - Axis along which to concatenate. Default is 0.

    @return Array with same shape as mat1 and concatenate along axis

    """
    return np.concatenate((mat1, mat2), axis)
