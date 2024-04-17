#!/usr/bin/python3
"""The module updates a file"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts in  middle of a file
    Args:
        filename(str): name of the file
        search_string(str): the string to search within the file
        new_string(str): the new string to append
    Return:
        None
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)
    except FileNotFoundError:
        print(f"Error: FIleNotFoundError '{filename}'")
