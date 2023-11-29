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
    
    if result_tuple[0] < 2:
        return (0, 0)
    else:
        return (result_tuple)


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    result = add_tuple(tuple_a, tuple_b)
