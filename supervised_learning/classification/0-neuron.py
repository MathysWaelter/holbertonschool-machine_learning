#!/usr/bin/env python3

"""defines a single neuron performing binary classification"""
import numpy as np


class Neuron:
    def __init__(self, nx):
        """
         Initialize the parameters of the random walk.

         @param nx - number of nodes in the walk (must be positive)
        """

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0

        # nx is an integer.
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        # nx must be a positive integer
        if nx < 1:
            raise ValueError("nx must be a positive integer")
