#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    a = 0
    for i in dir(hidden_4):
        if (i.startswith("__") is False):
            print(dir(hidden_4)[a])
        a = a + 1
