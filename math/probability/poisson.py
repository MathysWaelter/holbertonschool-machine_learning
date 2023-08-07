#!/usr/bin/env python3


"""initialize poisson class"""


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
