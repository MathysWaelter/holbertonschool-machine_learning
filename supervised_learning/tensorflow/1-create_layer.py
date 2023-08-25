#!/usr/bin/env python3
"""create_layer"""

import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """
    Creates a new layer in a neural network.
    """
    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')

    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=initializer,
                            name='layer')(prev)
    return layer
