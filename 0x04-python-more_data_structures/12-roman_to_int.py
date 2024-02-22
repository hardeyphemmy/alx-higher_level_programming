#!/usr/bin/python3

def roman_to_int(roman_string):
    """Convert roman to integer."""
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and roman_numerals[roman_string[i]]\
                < roman_numerals[roman_string[i + 1]]:
            result -= roman_numerals[roman_string[i]]
        else:
            result += roman_numerals[roman_string[i]]

    return result


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
