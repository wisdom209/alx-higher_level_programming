#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Function that computes the square value of all integers of a matrix.

    Args:
            matrix (list, optional): List of integers. Defaults to [].

    Returns:
            List: list containing squares of matrix elements
    """

    if (matrix):
        return list(map(lambda inner_list: [x**2 for x in inner_list], matrix))
