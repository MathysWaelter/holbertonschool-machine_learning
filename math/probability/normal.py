#!/usr/bin/env python3


"""exponential probability calcul"""

e = 2.7182818285


class Normal:
    """
    class for normal probality
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize the Lamtha estimator.
        @param data - list of values to be used for estimating
        @param stddev - lambda value to
        """
        # The stddev of the data.
        if data is None:
            # Raised if stddev is negative.
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            # TypeError if data is not a list
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            # Raise ValueError if len data 2
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)

            variance = sum([(x - self.mean) ** 2 for x in data]) / len(data)

            self.stddev = variance ** 0.5

    def z_score(self, x):
        """calcul z score with x"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """calcul x value with z value"""
        return self.mean + (z * self.stddev)
