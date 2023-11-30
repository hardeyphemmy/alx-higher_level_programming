#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function that print the biggest integer
    Return:
    If list is empty, None
    """
    if not my_list:
        return (None)

    max_number = my_list[0]
    for number in my_list[1:]:
        if number > max_number:
            max_number = number

    return (max_number)


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, 99, -13, 3]
    max_number = max_integer(my_list)

    print("Max: {}".format(max_number))
