#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Function that finds all multiples of 2 in a list
    Arg:
    my_list (list) integers in a list
    Return:
    True if list is divisible by 2, False otherwise
    """
    result_list = [element % 2 == 0 for element in my_list]
    return (result_list)


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    result = divisible_by_2(my_list)

    for element, is_divisible in zip(my_list, result):
        if is_divisible:
            print("{:d} is divisible by 2".format(element))
        else:
            print("{:d} is not divisible by 2".format(element))
