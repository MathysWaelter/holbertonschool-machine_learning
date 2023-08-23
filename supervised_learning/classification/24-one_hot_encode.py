#!/usr/bin/env python3
"""defines a encode method"""

import numpy as np


def one_hot_encode(Y, classes):
    """
     One hot encode the labels.
     @param Y -  array of class labels
     @param classes - number of classes in the training set
     @return - array of one hot
    """
    m = Y.shape[0]
    encoded_labels = np.zeros((classes, m))

    # Set the encoded labels for each class label.
    for i in range(m):
        class_label = Y[i]
        encoded_labels[class_label, i] = 1

    return encoded_labels
