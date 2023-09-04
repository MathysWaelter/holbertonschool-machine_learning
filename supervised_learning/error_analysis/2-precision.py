#!/usr/bin/env python3
"""precision of a confusion matrix"""

import numpy as np


def precision(confusion):
    """calcul precision of a confusion matrix"""

    correct_label = np.diag(confusion)
    predicted_label = np.sum(confusion, axis=0) - correct_label
    precision_value = correct_label / (predicted_label + correct_label)

    return precision_value
