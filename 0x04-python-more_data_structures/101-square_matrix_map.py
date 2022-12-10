#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda inner_list: [x**2 for x in inner_list], matrix))
