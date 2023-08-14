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
