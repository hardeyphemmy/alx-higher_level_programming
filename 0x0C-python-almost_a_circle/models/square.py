#!/usr/bin/python3
"""The model Square inherited from Rectangle."""

from models.rectangle import Rectangle


class Square(Base):
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
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for attr, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs["id"]
                if 'size' in kwargs:
                    self.size = kwargs["size"]
                if 'x' in kwargs:
                    self.x = kwargs["x"]
                if 'y' in kwargs:
                    self.y = kwargs["y"]
        return self

    def to_dictionary(self):
        """Return dictionary representation of square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
