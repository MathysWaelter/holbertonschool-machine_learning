#!/usr/bin/env python3
"""defines a decode method"""

import numpy as np


def one_hot_decode(one_hot):
    """
     Decodes one hot encoding.
     @param one_hot - A 2D NumPy array of shape
     @return A 1D NumPy array of shape
    """
    try:
        decoded_labels = np.argmax(one_hot, axis=0)
        return decoded_labels
    except:
        return None
