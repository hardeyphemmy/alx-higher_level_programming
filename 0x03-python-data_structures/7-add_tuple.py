#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Function that adds two tuples
    Args:
    tuple_a: Element in the First arg
    tuble_b: Element in the second arg
    Return:
    Tuple with 2 integers
    """
    result_tuple = tuple(a + b for a, b in zip(tuple_a, tuple_b))
    print(result_tuple)

    # check the length of tuple
    element_a = tuple_a[0] if len(tuple_a) >= 1 else 0
    element_b = tuple_b[0] if len(tuple_b) >= 1 else 0

    element_c = tuple_a[1] if len(tuple_a) > 2 else 2
    element_d = tuple_b[1] if len(tuple_b) > 2 else 2

    result_tuple = (element_a + element_b, element_c + element_d)

    # if a tuple is smaller than 2, use the value 0 for each missing integer
    """if any(x < 2 for x in tuple_a or any(x < 2 for x in tuple_b)):
        return (0)
    else:
        return (result_tuple)"""


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    result = add_tuple(tuple_a, tuple_b)
