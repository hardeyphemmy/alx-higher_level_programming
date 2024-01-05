#!/usr/bin/python3
"""How to access and update private attribute."""


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


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
