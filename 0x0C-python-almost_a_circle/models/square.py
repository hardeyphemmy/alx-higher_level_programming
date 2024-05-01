#!/usr/bin/python3
"""The model Square inherited from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The class inherit from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """The function initialize a square
        Args:
            size(int): The size of the square
            x(int): The x-coordinate of the square
            y(int): The y-coordinate of the square
            id(int): The identifier of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """square getter size."""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """Update class  with ardument and keyword arguments
        Args:
            1st args = id
            2nd args = size
            3rd args = x
            4th args = y
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
            else:
                for attr, value in kwargs.items():
                    if attr in self.__dict__.key():
                        setattr(self, attr, value)
