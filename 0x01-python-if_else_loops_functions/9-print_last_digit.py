#!/usr/bin/python3
def print_last_digit(number):
    last_digit = (abs(number) % 10)
    print("{}".format(number))


if __name__ == "__main__":
    print_last_digit(98)
