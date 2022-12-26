#!/usr/bin/python3
"""This module divides a matrix"""
import doctest


def matrix_divided(matrix, div):
    """Divides matrix elements by div
       and returns a new matrix

    Args:
        matrix (list): `matrix`
        div (list): `div`
    return:
        new_matrix (list): new matrix from operations
    """

    if (type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for x in matrix:
        if type(x) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for y in x:
            if (type(y) is not float and type(y) is not int):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of " +
                    "integers/floats")

    matrix_width = 0

    if (len(matrix[0])):
        matrix_width = len(matrix[0])

    for x in matrix:
        if (type(x) is list):
            if len(x) != matrix_width:
                raise TypeError(
                    "Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    sub_list = []
    new_matrix = []
    for x in matrix:
        for y in x:
            sub_list.append(y)
        new_matrix.append([round(i/div, 2) for i in sub_list])
        sub_list = []
    return new_matrix


if __name__ == '__main__':
    doctest.testfile("./tests/2-matrix_divided.txt")
