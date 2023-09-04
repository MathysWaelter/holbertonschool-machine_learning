#!/usr/bin/env python3
"""confusion matrix"""

import numpy as np


def create_confusion_matrix(labels, logits):
    """create confusion matrix"""
    classes = labels.shape[1]

    confusion = np.zeros((classes, classes), dtype=np.int32)

    for i in range(labels.shape[0]):
        correct_label = np.argmax(labels[i])
        predicted_label = np.argmax(logits[i])

        confusion[correct_label][predicted_label] += 1

    return confusion
