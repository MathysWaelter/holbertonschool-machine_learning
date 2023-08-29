#!/usr/bin/env python3
"""normalization"""


import numpy as np
import tensorflow.compat.v1 as tf


def normalization_constants(X):
    """calculates the normalization (standardization) constants of a matrix"""
    mean = np.mean(X, axis=0)
    std_dev = np.std(X, axis=0)
    return mean, std_dev
