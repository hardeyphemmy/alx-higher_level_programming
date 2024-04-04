#!/usr/bin/python3
"""The module defines a class checking function"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is exactly an instance of a given class

    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj of an instance
    Returns:
        bool: True If obj is exaclty an instance of a_class, False otherwise
    """

    return isinstance(obj, a_class)


if __name__ == "__main__":
    is_same_class = __import__('2-is_same_class').is_same_class

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
