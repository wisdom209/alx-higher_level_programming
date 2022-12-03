#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    x_a = 0
    y_a = 0
    x_b = 0
    y_b = 0

    if (a_len == 1):
        x_a = tuple_a[0]
    elif (a_len == 2):
        x_a, y_a = tuple_a
    elif (a_len != 0):
        x_a, y_a, *_ = tuple_a

    if (b_len == 1):
        x_b = tuple_b[0]
    elif (b_len == 2):
        x_b, y_b = tuple_b
    elif (b_len != 0):
        x_b, y_b, *_ = tuple_b

    new_tuple = (x_a + x_b, y_a + y_b)

    return new_tuple
