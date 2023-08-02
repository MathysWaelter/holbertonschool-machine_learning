#!/usr/bin/env python3


"""Summation of i squared."""
import numpy as np


def summation_i_squared(n):
    """
    @param n - number of integers to calculate
    @return sum of squares of
    """
    array = np.arange(1, n + 1)
    result = np.sum(array ** 2)
    return result
