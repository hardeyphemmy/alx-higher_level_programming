#!/usr/bin/python3
"""This module load,add and save to a file"""

import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


def save_to_json_file(*args):
    """
    This function is to save argument to a python file to a file
    named 'add_item.json'.
    Args:
        *args: argument list to be saved
    """
    arguments_list = list(args)
    save_to_json_file(arguments_list, "add_item.json")


def load_from_json_file():
    """This function loads arguments from a named file 'add_item.json'.
    Returns
        list: The list of argument loaded from the file
    """
    return load_from_json_file("add_item.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python script.py arg1 agr2 ...")
        sys.exit(1)

        arguments = sys.argv[1:]

        save_arguments_to_file(*arguments)
        print("Arguments saved to add_item.json")

        loaded_arguments = load_arguments_from_file()
        print("Arguments loaded from file:", loaded_arguments)
