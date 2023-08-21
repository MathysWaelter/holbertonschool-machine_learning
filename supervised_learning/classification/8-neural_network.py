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
        if nx <= 0:
            raise ValueError("nodes must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        # nodes must be a positive integer
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
