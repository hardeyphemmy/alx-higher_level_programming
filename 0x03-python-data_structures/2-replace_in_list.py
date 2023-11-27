#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an elemnt of a list.
    Args:
    my_list: The list from from the element.
    idx: index from the element to replace
    new_element: The number to replace
    Returns:
    The original list
    """

    if 0 <= idx < len(my_list):
        my_list[idx] = new_element
    return (my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 1
    new_element = 4

    new_list = replace_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)
