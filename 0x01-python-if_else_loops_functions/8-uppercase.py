#!/usr/bin/python3
"""Function that prints a string in uppercase followed by a new line"""


def uppercase(str):
    for c in str:
        num = ord(c)
        if num >= 65 and num <= 90:
            print(c, end="")
        elif num >= 97 and num <= 122:
            num = num - 32
            c = chr(num)
            print(c, end="")
        else:
            print(c, end="")
    print()


if __name__ == "__main__":
    uppercase("Best# School 98 Battery street")
