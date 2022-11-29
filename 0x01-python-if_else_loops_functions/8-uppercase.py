#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        new_str_char = ord(str[i])

        if (str[i] == ' '):
            new_str_char = 32
        elif (new_str_char >= ord('a') and new_str_char <= ord('z')):
            new_str_char = ord(str[i]) - 32

        print("{0:c}".format(new_str_char), end="")

    print("".format())
