#!/usr/bin/python3
"""The module for printing a square."""


class Square:
    """This is a squared class."""

    def __init__(self, size=0):
        """The constructor of the class."""
        self.__size = size

    @property
    def size(self):
        """Property getter to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """This method returns the square of an area."""
        return self.size ** 2

    def my_print(self):
        """"This method prints square with character '#'."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
