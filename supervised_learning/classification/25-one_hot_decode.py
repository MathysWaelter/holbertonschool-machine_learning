#!/usr/bin/env python3
"""defines a decode method"""

import numpy as np


def one_hot_decode(one_hot):
    """
     Decodes one hot encoding.
     @param one_hot - A 2D NumPy array of shape
     @return A 1D NumPy array of shape
    """
    if not isinstance(one_hot, np.ndarray):
        return None
    if len(one_hot) == 0 or len(one_hot.shape) != 2:
        return None
    return np.argmax(one_hot, axis=0)
