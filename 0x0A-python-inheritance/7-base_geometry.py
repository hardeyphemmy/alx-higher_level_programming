#!/usr/bin/python3
"""The module defines the BaseGeometry"""


class BaseGeometry:
    """The class function of BaseGeometry.

    Calculate the area.

    Raises:
        Exception: If the area calculation is not impemented.
    """

    def area(self):
        raise NotImplementedError("area() is not implemented")


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


if __name__ == "__main__":
    BaseGeometry = __import__('7-base_geometry').BaseGeometry

    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
