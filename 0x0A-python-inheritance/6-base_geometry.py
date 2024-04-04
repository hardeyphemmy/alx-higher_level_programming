#!/usr/bin/python3
"""The module that improve geometry"""


class BaseGeometry:
    """The class function of BaseGeometry.

    Calculate the area.

    Raises:
        Exception: If the area calculation is not impemented.
    """

    def area(self):
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
