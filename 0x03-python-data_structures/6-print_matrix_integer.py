#!/usr/bin/python3
if __name__ == '__main__':
    def print_matrix_integer(matrix=[[]]):
        for a_list in matrix:
            a = 0
            list_len = len(a_list)

            if len(a_list) == 0:
                print()
            else:
                for x in a_list:
                    if a == list_len - 1:
                        print("{0:d}".format(x))
                    else:
                        print("{0:d}".format(x), end=" ")
                    a = a + 1
