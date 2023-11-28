#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.
    Args:
    my_string (str): Input string
    new_string (str): Modified string
    Returns:
    Modified string with 'c' and 'C' removed
    """
    return ''.join(char for char in my_string if char.lower() not in {'c', 'C'})


if __name__ == "__main__":
    my_string = "Best School"
    new_string = no_c(my_string)
    print(new_string)
