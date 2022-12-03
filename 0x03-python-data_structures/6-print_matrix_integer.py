#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for a_list in matrix:
            a = 0
            list_len = len(a_list)

            if len(a_list) == 0:
                print("".format())
            else:
                for x in a_list:
                    if a == list_len - 1:
                        print("{:d}".format(x))
                    else:
                        print("{:d}".format(x), end=" ")
                    a = a + 1
