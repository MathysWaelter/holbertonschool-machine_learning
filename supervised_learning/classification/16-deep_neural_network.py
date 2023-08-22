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
            if i <= 0:
                raise ValueError("layers must be a list of positive integers")
            
            He = np.random.randn(layers[i - 1], nx) * np.sqrt(2 / layers[i - 2])

            self.weights['W' + str(i)] = He
            self.weights['b' + str(i)] = np.zeros((layers[i - 1], 1))
            nx = layers[i - 1]
