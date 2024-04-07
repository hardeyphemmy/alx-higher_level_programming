#!/usr/bin/python3
"""The module defines file to read."""

def read_file(filename=""):
    """
    read a text file UTF8 and prints it to stdout
    Args:
        filename(str): The name of the file to read
    Raises:
        FileNotFoundError: If the exact file do not exist
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")


if __name__ == "__main__":
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")

    print("\nWe offer a truly innovative approach to education:\n"
    "focus on building reliable applications and scalable systems,\n"
    "take on real-world challenges, collaborate with your peers.\n\n"

    "A school every software engineer would have dreamt of!")
