#!/usr/bin/env python3
"""L2_regularizatio"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """update cost with L2"""
    l2 = 0
    for i in range(L):
        l2 += np.sum(weights.get("W{}".format(i + 1))**2)

    return cost + (lambtha / (2 * m)) * l2
