#!/usr/bin/env python3

"""defines a neural network with one hidden
layer performing binary classification"""
import numpy as np


class NeuralNetwork:
    """ Initialize the parameters of the random walk."""
    def __init__(self, nx, nodes):
        """
        @param nx - number of nodes in the walk (must be positive)
        """
        # nx is an integer.
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        # nx must be a positive integer
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        # nodes must be a positive integer
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        Getter for W1
        """
        return self.__W1

    @property
    def b1(self):
        """
        Getter for b1
        """
        return self.__b1

    @property
    def A1(self):
        """
        Getter for A1
        """
        return self.__A1

    @property
    def W2(self):
        """
        Getter for W2
        """
        return self.__W2

    @property
    def b2(self):
        """
        Getter for b2
        """
        return self.__b2

    @property
    def A2(self):
        """
        Getter for A2
        """
        return self.__A2

    def forward_prop(self, X):
        """
         Forward propagation of the neural network.
         @param X - ( n d ) array of data
         @return ( n ) array of activation of neuron at each
        """
        Z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))
        Z2 = np.dot(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))
        return self.__A1, self.__A2

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
        hidden, A = self.forward_prop(X)
        C = self.cost(Y, A)
        return np.where(A >= 0.5, 1, 0), C