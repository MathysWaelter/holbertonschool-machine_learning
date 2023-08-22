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
        if not layers or not isinstance(layers, list):
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for l in range(1, self.L + 1):
            if not isinstance(layers[l - 1], int) or layers[l - 1] <= 0:
                raise TypeError("layers must be a list of positive integers")
            W = np.random.randn(layers[l - 1], nx) * np.sqrt(2/nx)
            b = np.zeros((layers[l - 1], 1))
            self.weights['W' + str(l)] = W
            self.weights['b' + str(l)] = b
            nx = layers[l - 1]

    @property
    def L(self):
        """
         Getter for L
         @return L
        """
        return self.__L

    @property
    def cache(self):
        """
         Getter for the cache.
         @return The cache to use for this test case
        """
        return self.__cache

    @property
    def weights(self):
        """
         Returns the weights associated with this node.
         @return A dictionary mapping node names
        """
        return self.__weights

    def forward_prop(self, X):
        """
         Forward propagation of the neural network.
         @param X - ( n d ) array of data
         @return ( n ) array of activation of neuron at each
        """
        self.__cache = {'A0': X}
        A = X
        for i in range(1, self.__L + 1):
            A_prev = A
            W = self.__weights['W' + str(i)]
            b = self.__weights['b' + str(i)]

            Z = np.dot(W, A_prev) + b
            A = 1 / (1 + np.exp(-Z))

            self.__cache['A' + str(i)] = A

        return A, self.__cache
