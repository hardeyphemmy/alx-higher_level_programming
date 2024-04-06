#!/usr/bin/python3
"""This is a module to add attribute"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    # Check if the object is a dictionary or has __dict__ attribute
    if hasattr(obj, '__dict__') or isinstance(obj, dict):
        obj.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")


if __name__ == "__main__":
    add_attribute = __import__('101-add_attribute').add_attribute

    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
