#!/usr/bin/python3
"""The module defines a class checking function."""


def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a class that inherited
    from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a sublass that inherited
        from a_class, False otherwise.
    """
    # Get the class of the object
    obj_class = obj.__class__

    # Check if the object's class is a subclass of a_class
    return issubclass(obj_class, a_class)


if __name__ == "__main__":
    inherits_from = __import__('4-inherits_from').inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
