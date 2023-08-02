#!/usr/bin/env python3

"""Returns the derivative of a polynomial."""


def poly_derivative(poly):
    """
    @param poly - The polynomial to be differentiated.
    @return The derivatives of the polynomial
    """
    # Return None if poly is a list or len poly.
    if not isinstance(poly, list) or len(poly) is None:
        return None

    coeff = []

    # Add derivative to coeff array
    for i, x in enumerate(poly[1:], start=1):
        coeff.append(x * i)

    if all(coeff):
        return [0]

    return coeff
