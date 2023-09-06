#!/usr/bin/env python3
"""f1_score"""

import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """calculate f1_score"""
    return (2 * (precision(confusion) * sensitivity(confusion)) /
            (precision(confusion) + sensitivity(confusion)))
