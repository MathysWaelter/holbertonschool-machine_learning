#!/usr/bin/env python3
"""Shuffle"""

import numpy as np


def shuffle_data(X, Y):
    """permutation"""
    permutation = np.random.permutation(X.shape[0])
    X_shuffled = X[permutation]
    Y_shuffled = Y[permutation]
    return X_shuffled, Y_shuffled
