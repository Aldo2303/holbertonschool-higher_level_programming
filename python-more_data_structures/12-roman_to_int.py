#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or None:
        return 0
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    decimal_result = 0
    prev_value = 1000
    for i in roman_string:
        value = roman_numbers.get(i, 0)
        if value <= prev_value:
            decimal_result += value
        else:
            decimal_result += value - prev_value*2
        prev_value = value
    return (decimal_result)
