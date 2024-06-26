#!/usr/bin/python3
"""This module return class to JSON"""


def class_to_json(obj):
    """The function returns python class to json
    Args:
        obj(str): An instance of a class
    REturn:
        The dictionary description with simple data structure
    """

    """Get the attribute of the object"""
    attribute = obj.__dict__
    """New dictionary to store processed attribute"""
    result = {}
    """Iterate over the attributes"""
    for key, value in attribute.items():
        """check the type of the value"""
        if isinstance(value, (list, dict, str, int, bool)):
            """If value is a simple data type add to result dictionary"""
            result[key] = value
        else:
            """if value is not simple data type convert to to a string"""
            result[key] = str(value)

    return result
