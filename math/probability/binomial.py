#!/usr/bin/env python3


"""binomial probability calcul"""

e = 2.7182818285
pi = 3.1415926536


def facto(n):
    """calcul factorial"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


class Binomial:
    """
    class for binomial probality
    """
    def __init__(self, data=None, n=1, p=0.5):
        """
        @param data - list of values to be used for estimating
        @param n - number of Bernoulli trials
        @param p - probability of a “success
        """
        if data is None:
            # Raised if p is negative.
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.p = float(p)
            self.n = int(round(n))
        else:
            # TypeError if data is not a list
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            # Raise ValueError if len data 2
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.p = sum(data) / (len(data) * n)
            self.n = int(round(sum(data) / self.p) * 0.5)
            self.p = sum(data) / (len(data) * self.n)
