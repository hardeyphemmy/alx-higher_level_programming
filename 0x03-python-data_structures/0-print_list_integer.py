#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        for number in my_list:
            if isinstance(number, int):
                print(["{:d}"].format(number), end=', ')
        print()


my_numbers = [1, 2, 3, 4, 5]
print_list_integer(my_list)
