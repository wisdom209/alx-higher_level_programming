#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a roman numberal to digits

    Args:
        roman_string (str): roman nummeral

    Returns:
        int: roman numeral in digits
    """    
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    sum = 0
    strlen = len(roman_string)
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum_list = []

    for i in range(strlen):
        sum_list.append(roman_dict[roman_string[i]])

    for i in range(strlen):
        if (i != strlen - 1 and sum_list[i] < sum_list[i + 1]):
            sum = sum - sum_list[i]
        else:
            sum = sum + sum_list[i]
    return sum

