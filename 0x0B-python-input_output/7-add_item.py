#!/usr/bin/python3
"""This module load,add and save to a file"""

import sys
import json

""" Load functions from previous exercises"""
def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Loads a JSON object from a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file '{filename}' not found")

"""Create a list from command-line arguments"""
args = sys.argv[1:]
args_list = args

"""Save the list to a JSON file named 'add_item.json'"""
filename = 'add_item.json'
save_to_json_file(args_list, filename)
print(f"Arguments saved to {filename}")

""" Load the list from the JSON file"""
loaded_list = load_from_json_file(filename)
print(f"Loaded list from {filename}:")
print(loaded_list)
