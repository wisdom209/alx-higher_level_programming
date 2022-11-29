#!/usr/bin/python3
def print_reverse():
    for i in range(122, 96, -1):
        if (i % 2 == 0):
            print("{0:c}".format(i), end="")
        else:
            print("{0:c}".format(i-32), end="")


print_reverse()
