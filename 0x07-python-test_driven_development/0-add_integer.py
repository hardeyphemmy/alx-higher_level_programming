#!/usr/bin/python3
def add_integer(a, b=98):
    """The methods that add two numbers.

    Args:
    a and b must be integers or floats, a and b must be first
    casted to integers if they are float.

    Returns
    an integer: the addition of a and b."""

    if not (isinstance(a, (int, float))):
        raise TypeError("'a' must be either integer or a float")
    if not (isinstance(b, (int, float))):
        raise TypeError("'b' must be either integer or a float")
    # convert a and b to integer
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return (a + b)

    # Ensure 'b' is an integer
    if not isinstance(b, int):
        raise TypeError("'b' must be an integer")
    return (a + b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
