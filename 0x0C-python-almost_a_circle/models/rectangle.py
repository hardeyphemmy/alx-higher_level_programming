#!/usr/bin/python3
"""The module of rectangle"""

from models.base import Base


class Rectangle(Base):
    """The class rectangle inherited from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function initialize the rectangle
        Args:
            width(int): The length of the rectangle
            height(int): The height of the rectangle
            x(int): undefined value
            y(int): undefined value
        Return:
            results
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width private instance attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width private instance attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height private inatance attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height private instance attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the private instance attribute x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the private instance atribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the private instance attribute y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self__.y = value

    def area(self):
        """This function defines the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """This prints the Rectangle instance with '#' characters"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
