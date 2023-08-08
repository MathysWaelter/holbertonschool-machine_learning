#!/usr/bin/env python3


"""initialize poisson class"""

e = 2.7182818285


class Poisson:
    """
    class for poisson probality
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
            self.lambtha = float(sum(data) / len(data))

    def facto(self, n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def pmf(self, k):
        """
        Returns the probability mass function at k.
        @param k - number of trials to evaluate
        @return probability mass function at
        """
        self.k = float(k)
        self.e = e
        fact = 1

        # Convert k to an integer.
        if not isinstance(k, int):
            k = int(k)
        # Return k if k 0.
        if k < 0:
            return 0

        # Compute the fact of the first two k 1.
        for i in range(2, k+1):
            fact = fact * i

        return (e ** (- self.lambtha)) * (self.lambtha ** k) / fact

    def cdf(self, k):
        """Returns the probability density function at k.
        @param k - number of trials to evaluate
        @return probability mass function at
        """
        self.k = float(k)
        self.e = e
        cdf = 0.0

        if not isinstance(k, int):
            k = int(k)
        # Return k if k 0.
        if k < 0:
            return 0

        for x in range(0, k + 1):
            cdf += e ** (- self.lambtha) * (self.lambtha ** x) / self.facto(x)

        return cdf
