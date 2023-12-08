#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Frunction that replaces all occcurrences of an element by another
    new list
    Args:
    my_list - Element in a list
    search - finds multiple element
    replace - New element to be replaced
    Return:
    A new list
    """

    for idx, num in enumerate(my_list):
        if num == search:
            my_list = my_list.copy()
            my_list[idx] = replace

    return (my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
