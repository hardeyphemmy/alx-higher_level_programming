#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Function that adds all unique integers in a list
    Args:
    add - addition of integer in a list
    Returns:
    Sum of the unique integer
    """
    unique_elements = []
    for num in my_list:
        if num not in unique_elements:
            unique_elements.append(num)

    return sum(unique_elements)


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]

    result = uniq_add(my_list)

    print("Result: {}".format(result))
