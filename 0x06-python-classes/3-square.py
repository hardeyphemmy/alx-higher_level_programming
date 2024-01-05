#!/usr/bin/python3
"""This is an Area of square module."""


class Square:
    """This is a class of square."""
    def __init__(self, size=0):
        """This is a constructor of the class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """This is the method that returns square area"""
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
