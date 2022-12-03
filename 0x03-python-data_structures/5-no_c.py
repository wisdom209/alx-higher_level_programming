#!/usr/bin/python3
def no_c(my_string):
    new_string_list = []
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            new_string_list.append(my_string[i])
    return "".join(new_string_list)
