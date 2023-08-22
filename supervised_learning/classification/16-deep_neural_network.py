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

        for i in range(1, self.L + 1):
            current = layers[i - 1]
            He = np.random.randn(current, nx) * np.sqrt(2 / layers[i - 2])
            if not isinstance(current, int) or current <= 0:
                raise TypeError("layers must be a list of positive integers")

            self.weights['W' + str(i)] = He
            self.weights['b' + str(i)] = np.zeros((current, 1))
            nx = current
