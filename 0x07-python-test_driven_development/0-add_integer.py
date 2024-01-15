#!/usr/bin/python3
def add_integer(a, b=98):
    """The methods that add two numbers.

    a and b must be integers or floats, a and b must be first 
    casted to integers if they are float.

    Returns
    an integer: the addition of a and b."""
    
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both 'a' and 'b' must be either integer or a float")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
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
