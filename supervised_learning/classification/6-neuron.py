#!/usr/bin/env python3

"""defines a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """ Initialize the parameters of the random walk."""
    def __init__(self, nx):
        """
        @param nx - number of nodes in the walk (must be positive)
        """
        # nx is an integer.
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        # nx must be a positive integer
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
         Returns the weight matrix.
         @return The weight matrix for this node or None if not
        """
        return self.__W

    @property
    def b(self):
        """
         The B coordinate of the curve.
         @return The B coordinate of the curve or None if not
        """
        return self.__b

    @property
    def A(self):
        """
         The A value of the Brasshopper.
         @return The A value of the Brasshopper
        """
        return self.__A

    def forward_prop(self, X):
        """
         Forward propagation of the neural network.
         @param X - ( n d ) array of data
         @return ( n ) array of activation of neuron at each
        """
        Z = np.dot(self.W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

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
        A = self.forward_prop(X)
        C = self.cost(Y, A)
        return np.where(A >= 0.5, 1, 0), C

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
         Gradient descent for linear programming.

         @param X - The data of shape
         @param Y - The data of shape
         @param A - The vector of shape
         @param alpha
        """
        m = X.shape[1]
        dZ = A - Y
        dW = np.dot(X, dZ.T) / m
        db = np.sum(dZ) / m

        self.__W -= alpha * dW.T
        self.__b -= alpha * db

        return dW, db

    def update(dW, db, W, b, alpha):
        W = W - alpha * dW
        b = b - alpha * db
        return (W, b)

    def train(self, X, Y, iterations=5000, alpha=0.05):

        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        # Evaluate the gradient descent for X and Y. This is a recursive method
        for _ in range(iterations):
            A = self.forward_prop(X)
            self.gradient_descent(X, Y, A, alpha)

        return self.evaluate(X, Y)
