#!/usr/bin/python3
def add_integer(a, b=98):
    """The methods that add two numbers.

    Args:
    a and b must be integers or floats, a and b must be first
    casted to integers if they are float.

    Raises
    TypeError: If either of a or b is a non-integer and non-float."""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("'a' must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a)) + (int(b))
