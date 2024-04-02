#!/usr/bin/python3
"""This is the function to set name."""


def say_my_name(first_name, last_name=""):
    """ Print my names

    Arg:
        first_name (str): The first name to print
        last_name (str): The last name to print

    Raise:
        TypeError: If it is not a string."""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be string")

    print("My name is {} {}".format(first_name, last_name))
