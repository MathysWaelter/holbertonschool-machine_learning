#!/usr/bin/env python3
"""sensitivity of a confusion matrix"""

import numpy as np


def sensitivity(confusion):
    """calcul sensitivity of a confusion matrix"""

    correct_label = np.diag(confusion)
    predicted_label = np.sum(confusion, axis=1) - correct_label
    sensitivity_value = correct_label / (predicted_label + correct_label)

    return sensitivity_value
