#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            if (i == x - 1):
                print()
            num_printed += 1
    except IndexError as err:
        print()
    except Exception as err:
        print()
    return num_printed
