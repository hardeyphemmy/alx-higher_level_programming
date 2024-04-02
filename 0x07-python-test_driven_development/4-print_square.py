#!/usr/bin/python3
"""The module defining a square ."""


def print_square(size):
    """The function prints a square with # characters.

    Arg:
        size (int): the height and width

    raise:
        ValueError: If size is less than 0
        TypeError: If size is a float and less than 0."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
