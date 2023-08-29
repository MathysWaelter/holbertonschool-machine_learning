#!/usr/bin/env python3
"""Shuffle"""

import numpy as np


def shuffle_data(X, Y):
    """permutation"""
    X = np.random.permutation(X)
    Y = np.random.permutation(Y)
    return X, Y
