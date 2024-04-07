#!/usr/bin/python3
"""Module that write a text file"""


def write_file(filename="", text=""):
    """The function write a file encoding with 'utf-8'
    Args:
        filename(str): The name of the file to write
    Return:
        The number of character written
    """

    with open(filename, "w", encoding="utf-8") as file:
        content = file.write(text)
    return content


if __name__ == "__main__":
    write_file = __import__('1-write_file').write_file

    b_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(b_characters)
