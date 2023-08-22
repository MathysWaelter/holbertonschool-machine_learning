#!/usr/bin/env python3
"""defines a deep neural network"""

import numpy as np


class DeepNeuralNetwork:
    """ Initialize the parameters."""

    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list):
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for l in range(1, self.L + 1):
            if not isinstance(layers[l - 1], int) or layers[l - 1] <= 0:
                raise TypeError("layers must be a list of positive integers")
            W = np.random.randn(layers[l - 1], nx) * np.sqrt(2/nx)
            b = np.zeros((layers[l - 1], 1))
            self.weights['W' + str(l)] = W
            self.weights['b' + str(l)] = b
            nx = layers[l - 1]
