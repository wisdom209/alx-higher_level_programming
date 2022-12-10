#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda a_list: list(map(lambda x: x**2, a_list)), matrix))
