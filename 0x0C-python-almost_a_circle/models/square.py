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

    def _str_(self):
        """Return a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)
