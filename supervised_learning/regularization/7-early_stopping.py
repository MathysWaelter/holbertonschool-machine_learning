#!/usr/bin/env python3
"""early stop"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """early stoping"""
    if opt_cost - cost > threshold:
        count = 0
    else:
        count += 1
    return count == patience, count