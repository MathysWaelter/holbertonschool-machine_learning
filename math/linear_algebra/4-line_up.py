#!/usr/bin/env python3

"""Add two arrays of same length and return sum of them."""


def add_arrays(arr1, arr2):
    """
    @param arr1 - first array to be added
    @param arr2 - second array to be added to first array

    @return sum of arr1 and arr2 or None if length doesn't match
    """
    res = []
    lenght = len(arr1)

    # Returns None if the length of the two arrays is not equal.
    if len(arr1) != len(arr2):
        return None

    # appends the result to the res. append arr1 arr2
    for j in range(lenght):
        res.append(arr1[j] + arr2[j])
    return res
