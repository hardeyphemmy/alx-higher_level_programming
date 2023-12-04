#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Fuction that deletes item from the list and modify the original list
    Args:
    my_list: list of element
    idx: elemnt to be delected
    Return:
    Same list
    """
    if 0 <= idx < len(my_list):
        modified_list = (my_list[:idx])
        return (modified_list, modified_list.copy())
    else:
        return (my_list.copy(), my_list.copy())


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    my_new_list, modified_list = delete_at(my_list, idx)

    print(modified_list)
    print(my_new_list)
