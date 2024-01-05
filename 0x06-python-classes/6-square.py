#!/usr/bin/python3
"""This is a module of squares."""


class Square:
    """This is a class of square."""
    def __init__(self, size=0, position=(0, 0)):
        """This is a constructor method."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property getter to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size  must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Property getter to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter to set position."""
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(i, int) for i in value) or any(
                        i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """This is the method returns current square area."""
        return self.size ** 2

    def my_print(self):
        """This method prints the square with the character '#'."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()
