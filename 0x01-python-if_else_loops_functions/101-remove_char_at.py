#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = []
    if (n < 0 or n > len(str)):
        return (str)
    for i in range(0, len(str) - 1):
        newstr.append('x')
    for i in range(0, len(str) - 1):
        if (i < n):
            newstr[i] = str[i]
        else:
            newstr[i] = str[i + 1]
    return (''.join(newstr))
