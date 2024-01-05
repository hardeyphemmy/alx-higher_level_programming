#!/usr/bin/python3
"""This is a size validation."""


class Square:
    """This ia a class of square."""
    def __init__(self, size=0):
        """This is the constructor of the class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)
