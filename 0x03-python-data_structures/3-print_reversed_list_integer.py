#!/usr/bin/python3
if __name__ == '__main__':
    def print_reversed_list_integer(my_list=[]):
        my_list.reverse()
        for i in my_list:
            print("{0:d}".format(i))
