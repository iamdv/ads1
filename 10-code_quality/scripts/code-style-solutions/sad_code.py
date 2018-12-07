"""
You need to refactor the function zero_insert to pass
the pep8 and pylint checks
"""

import numpy as np


def zero_insert(elements, number_of_zeros):
    """
    Takes in a vector and returns a new vector where
    every element is separated by a specified number
    of consecutive zeros.
    :param elements: input vector
    :param number_of_zeros: number of zeroes to separate the elements
    :return: input vector with elements separated by zeros
    """
    result_array = np.array([])
    zeros = np.zeros(number_of_zeros)
    for i in np.arange(0, len(elements)):
        result_array = np.append(result_array, elements[i])
        if i < len(elements) - 1:
            result_array = np.append(result_array, zeros)
    return result_array


if __name__ == "__main__":
    print(zero_insert([1, 2, 3, 4, 5], 4))
