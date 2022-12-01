#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if (argc != 0):
        if (argc == 1):
            print(f"{argc} argument:")
        else:
            print(f"{argc} arguments:")
        for i in range(argc):
            print(f"{i + 1}: {sys.argv[i + 1]}")
    else:
        print("0 arguments.")
