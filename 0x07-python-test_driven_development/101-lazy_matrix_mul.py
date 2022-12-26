#!/usr/bin/python3
"""This module multiplies two matrices with numpy lib"""
import numpy as np
import doctest


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
        m_a (list): matrix a
        m_b (list): matric b

    Raises:
        TypeError: m_a must be a list
        TypeError: m_b must be a list
        TypeError: m_a must be a list of lists
        TypeError: m_b must be a list of lists
        ValueError: m_a can't be empty
        ValueError: m_b can't be empty
        TypeError: m_a should contain only integers or floats
        TypeError: m_b should contain only integers or floats
        TypeError: each row of m_a must be of the same size"
        TypeError: each row of m_b must be of the same size"
        ValueError: m_a and m_b can't be multiplied

    Returns:
        list: matrix_a * matrix_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if i and type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if i and type(i) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_size = len(m_a[0])
    for i in m_a:
        if len(i) != row_size:
            raise TypeError("each row of m_a must be of the same size")

    row_size = len(m_b[0])
    for i in m_b:
        if len(i) != row_size:
            raise TypeError("each row of m_b must be of the same size")

    num_row_b = len(m_b)
    num_col_a = len(m_a[0])

    if (num_col_a != num_row_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b).tolist()


if __name__ == '__main__':
    doctest.testfile("./tests/101-lazy_matrix_mul.txt")
