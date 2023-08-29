#!/usr/bin/env python3
"""normalization"""

import numpy as np


def normalize(X, m, s):
    """standardize"""
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    X = (X - m) / s
    return X
