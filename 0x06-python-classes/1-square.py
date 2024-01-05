#!/usr/bin/python3
"""This is a square with private attribute."""


class Square:
    """This is a class of square."""
    def __init__(self, size):
        """This is the constructor of the class."""
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
