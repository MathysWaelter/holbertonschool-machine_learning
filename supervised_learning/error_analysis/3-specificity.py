#!/usr/bin/env python3
"""specificity of a confusion matrix"""

import numpy as np


def specificity(confusion):
    """specificity of a confusion matrix"""
    classes = confusion.shape[0]
    specificity_values = np.zeros(classes)

    for idx in range(classes):
        tpositif = confusion[idx][idx]
        fnegatif = np.sum(confusion[idx]) - tpositif
        fpositif = np.sum(confusion[:, idx]) - tpositif

        tnegatif = np.sum(confusion) - (tpositif + fpositif + fnegatif)

        specificity_values[idx] = tnegatif / (tnegatif + fpositif)

    return specificity_values
