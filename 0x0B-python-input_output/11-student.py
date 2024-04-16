#!/usr/bin/python3
"""This module define student and convert to JSON"""


class Student:
    """This is a class of a student"""

    def __init__(self, first_name, last_name, age):
        """This is the function that initalize a class
        Args:
            first_name(str): The first name of the student
            last_name(str): The last name of the student
            age(int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function retrieves a dictionary representation of a student
        Args:
            attrs: list of attributes names to retrieve
        Return:
            dict: DIctionary representation of the instance"""

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if
                    hasattr(self, attr)}

    def reload_from_json(self, json):
        """This function replace student from json
        Args:
            json(dict): Dictionary containing the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
