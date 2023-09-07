#!/usr/bin/env python3
"""L2_regularizatio"""

import tensorflow.compat.v1 as tf


def l2_reg_cost(cost):
    """calculates cost of a neural network with L2"""
    return cost + tf.losses.get_regularization_losses()
