#!/usr/bin/python3
"""The module defines the BaseGeometry"""


class BaseGeometry:
    """The class function of BaseGeometry.

    Calculate the area.

    Raises:
        Exception: If the area calculation is not impemented.
    """

    def __init__(self):
        """Initialize the BaseGeometry instance."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value making sure it is an integer.

        Args:
            name(str): The name of the value
            value(any): The value to validate

        Raises:
            TypeError exception if not an integer
            ValueError exception if not greater than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """The class Rectangle inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of a rectangle.
        """
        super().__init__()
        """Call the parent class __init__ method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle
        Retrns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle
        [Rectangle] <width/height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """This represent a class inherited from Rectangle"""

    def __init__(self, size):
        """Initialize with a Square instance with a size.
        Args:
            size(int): The size of the square.
        Raises:
            TypeError: If size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Calculate the area of square.
        Args:
            size(int): Length of a square
        Returns:
            (int):Area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """return the square representation.
        [square] <size/size>
        """
        return f"[square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    Square = __import__('11-square').Square

    s = Square(13)

    print(s)
    print(s.area())
