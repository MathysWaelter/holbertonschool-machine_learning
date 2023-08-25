#!/usr/bin/env python3
"""forward_prop"""

import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Creates the forward propagation graph for the neural network.
    """
    prev_layer = x

    for i in range(len(layer_sizes)):
        prev_layer = create_layer(prev_layer, layer_sizes[i], activations[i])

    return prev_layer
