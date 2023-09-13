#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0

    prev_value = 0
    for char in roman_string:
        value = roman_values.get(char, 0)
        if prev_value < value:
            result += value - (2 * prev_value)
        else:
            result += value

        prev_value = value

    return result
