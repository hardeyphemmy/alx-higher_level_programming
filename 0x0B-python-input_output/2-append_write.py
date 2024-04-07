#!/usr/bin/python3
"""This module is to append in python"""


def append_write(filename="", text=""):
    """This function is to append string at the end of a file
    Args:
        filename(str): The name of file to append
        text(str): The text to be appended to the file
    Return:
        The number of character added
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)


if __name__ == "__main__":
    append_write = __import__('2-append_write').append_write

    nb_characters_added = append_write("file_append.txt",
                                       "This School is so cool!\n")
    print(nb_characters_added)
