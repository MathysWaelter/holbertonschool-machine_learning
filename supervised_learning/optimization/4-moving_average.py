#!/usr/bin/env python3
"""average"""
import numpy as np


def moving_average(data, beta):
    """create a moving averages"""
    moving_averages = []
    vt = 0

    for x in data:
        vt = beta * vt + (1 - beta) * x
        biais = 1 - beta ** (len(moving_averages) + 1)
        moving_averages.append(vt / biais)

    return moving_averages
