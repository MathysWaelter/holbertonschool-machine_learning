#!/usr/bin/env python3


"""exponential probability calcul"""

e = 2.7182818285


class Exponential:
    """
    class for exponantial probality
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Initialize the Lamtha estimator.
        @param data - list of values to be used for estimating
        @param lambtha - lambda value to
        """
        # The lambtha of the data.
        if data is None:
            # Raised if lambtha is negative.
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            # TypeError if data is not a list
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            # Raise ValueError if len data 2
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(1.0 / (sum(data) / len(data)))

    def facto(self, n):
        """calcul factorial"""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def pdf(self, x):
        """
        Returns the probability mass function at k.
        @param k - number of trials to evaluate
        @return probability mass function at
        """
        self.e = e

        # Return k if k 0.
        if x < 0:
            return 0

        return self.lambtha * (e ** - (self.lambtha * x))

    def cdf(self, x):
        """Returns the probability density function at k.
        @param k - number of trials to evaluate
        @return probability mass function at
        """
        self.e = e
        cdf = 0.0

        # Return k if k 0.
        if x <= 0:
            return cdf

        cdf += 1 - (e ** (- self.lambtha * x))

        return float(cdf)
