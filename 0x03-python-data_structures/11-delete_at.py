#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Fuction that deletes item from the list
    Args:
    my_list: list of element
    idx: elemnt to be delected
    Return:
    New list
    """
    if 0 <= idx < len(my_list):
        return (my_list[:idx] + my_list[idx + 1:])
    else:
        return (my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_result = delete_at(my_list, idx)

    print(new_result)
    print(my_list)
