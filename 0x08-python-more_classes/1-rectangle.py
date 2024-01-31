#!/usr/bin/python3
"""This is a module of a rectangle."""


class Rectangle:
    """
    This is a class of a rectangle

    Attribute:
    width: The length of the rectangle
    height: The breath of the rectangle

    Arg:
    value: The integer assigned
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property to get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property to set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    try:
        my_rectangle1 = Rectangle(2, -3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

     try:
        my_rectangle2 = Rectangle(-2, 3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
