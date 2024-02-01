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

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str.rstrip()

    def __repr__(self):
        """Return a string representation to create new instance."""
        return f"Rectangle({self.__width}, {self.__height})"
