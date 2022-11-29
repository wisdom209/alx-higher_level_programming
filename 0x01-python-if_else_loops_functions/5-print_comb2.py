#!/usr/bin/python3
for i in range(100):
    print("{0:02d},".format(i), end=" ")
    if (i == 99):
        print("{0:d}".format(i))
