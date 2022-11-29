#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10

    if (number < 0):
        last_digit = ((number * -1) % 10)
    print(f"{last_digit:d}", end="")
    return (last_digit)
