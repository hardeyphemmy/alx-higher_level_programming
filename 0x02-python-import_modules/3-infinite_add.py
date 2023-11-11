#!/usr/bin/python3
import sys


def sum_arguments(arguments):
    total = 0
    for i, arg in enumerate(arguments):
        total += int(arg)

    print(total)


if __name__ == "__main__":
    sum_arguments(sys.argv[1:])
