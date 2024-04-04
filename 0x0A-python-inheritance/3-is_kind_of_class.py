#!/usr/bin/python3
"""The module defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a class or inherited
    from a specific class

    Args:
        obj(any): The object to check
        a_class(type): The class to check against
    Returns:
         bool: True If obj is exaclty an instance of a_class, False otherwise
    """

    return isinstance(obj, a_class)


if __name__ == "__main__":
    is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
