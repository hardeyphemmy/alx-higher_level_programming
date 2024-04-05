#!/usr/bin/python3
"""This is a module."""


class list:
    """This is a parent class list."""


class MyList(list):
    """This is a subclass of the list with additional method."""
    def __init__(self):
        """Initialize the MyList instance with an empty list."""
        super().__init__

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method assumes that all elements in the list are integers.
        """
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
