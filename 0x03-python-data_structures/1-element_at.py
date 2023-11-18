#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieve elements from the list.
    Args:
    my_list: The list from the element
    idx: index from the element to retrieve
    Returns:
    None if the index is negative, or None if element is out of range
    """

    if 0 <= idx < len(my_list):
        return (my_list[idx])
    else:
        return (None)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 2

    result = element_at(my_list, idx)
    if result is not None:
        print("Element at index {:d} is {}".format(idx, result))
    else:
        print(None)
