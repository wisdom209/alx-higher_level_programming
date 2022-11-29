#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number < 0:
    last_digit = ((number * - 1) % 10) * -1

str_first_part = f"Last digit of {number:d} is {last_digit:d}"

if last_digit > 5:
    print(f"{str_first_part} and is greater than 5")
if last_digit == 0:
    print(f"{str_first_part} and is 0")
if last_digit < 6 and last_digit != 0:
    print(
        f"{str_first_part} and is less than 6 and not 0")
