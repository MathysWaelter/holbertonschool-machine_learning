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

    def cost(self, Y, A):
        """
         Cost function for logistic regression.
        """
        m = Y.shape[1]
        return -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m

    def evaluate(self, X, Y):
        """
         Evaluate the cost function.
         @param X - The data points for which you want to evaluate
         @param Y - The target values for which you want to evaluate
         @return A tuple containing the cost function
        """
        A, cache = self.forward_prop(X)
        C = self.cost(Y, cache['A' + str(len(cache) - 1)])
        return np.where(cache['A' + str(len(cache) - 1)] >= 0.5, 1, 0), C

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
         Gradient descent for linear programming.

         @param X - The data of shape
         @param Y - The data of shape
         @param A - The vector of shape
         @param alpha
        """
        m = Y.shape[1]
        L = self.__L

        dZ = cache['A' + str(L)] - Y
        for i in range(L, 0, -1):
            last = cache['A' + str(i - 1)]
            dW = np.dot(dZ,  last.T) / m
            db = np.sum(dZ, axis=1, keepdims=True) / m
            dZ = np.dot(self.__weights['W' + str(i)].T,
                        dZ) * (last * (1 - last))
            self.__weights['W' + str(i)] -= alpha * dW
            self.__weights['b' + str(i)] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
         Train the neural network on the data and target.

         @param X - data matrix of shape [ n_samples n_features ]
         @param Y - target vector of shape [ n_samples ]
         @param iterations - number of iterations to perform gradient
         @param alpha - learning rate of gradient descent

         @return a tuple of the form ( X_new Y_new
        """
        # If iterations is not an integer raise TypeError
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        for _ in range(iterations):
            A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)

        return self.evaluate(X, Y)
