#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []

    if (idx < 0 or idx >= len(my_list)):
        new_list = [x for x in my_list]
        return new_list
    for i in range(len(my_list)):
        if (i == idx):
            new_list.append(element)
        else:
            new_list.append(my_list[i])
    return new_list
