#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for number in my_list:
        print("{}".format(number))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    my_list.reverse()
    print_reversed_list_integer()
    for number in my_list:
        print("{}".format(number), end='\n')
