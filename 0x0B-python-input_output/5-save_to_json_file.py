#!/usr/bin/python3
"""This module write and save a file using json"""

import json


def save_to_json_file(my_obj, filename):
    """
    This functions writes an object to a text file
    Args:
        my_obj(str): The object in a file
        filename(str0: The file to be save
    """
    if isinstance(my_obj, set):
        raise TypeError("Object of type set is not JSON serializable")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(my_obj, file)
    except PermissionError as e:
        raise PermissionError(f"[PermissionError] [Errno 13]\
                Permission denied: {filename}")


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
