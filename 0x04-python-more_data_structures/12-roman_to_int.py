#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str):
        return 0

    add = 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if i == len(roman_string) - 1:
            add += num[roman_string[i]]
        elif num[roman_string[i]] >= num[roman_string[i + 1]]:
            add += num[roman_string[i]]
        else:
            add -= num[roman_string[i]]
    return add
