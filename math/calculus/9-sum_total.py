#!/usr/bin/env python3


"""Summation of i squared."""


def summation_i_squared(n):
    """
    @param n - number of integers to calculate
    @return sum of squares of
    """
    if n < 0 or not isinstance(n, int):
        return None
    return int(n * (n + 1)*(2 * n + 1) / 6)
