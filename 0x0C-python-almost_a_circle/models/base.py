#!/usr/bin/python3
"""This is a module base."""
import json


class Base:
    """This is a class of all other classes in this project.
    manage attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class consructor for the Base class
        Args:
            id(int, optional): Id of the instance, if none assign new id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries
        Args:
            list_dictionaries(list): A list of dictionaries
        Returns:
            JSON string representation of the list of dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list of objects to a file
        Args:
            list_objs(list): A list of instance inheriting from the Base class
        """
        filename = cls.__name__ + ".json"
        json_string = []
        if list_objs is not None:
            for obj in list_objs:
                json_string.append(obj.to_dictionary())
        json_string = cls.to_json_string(json_string)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return list of the JSON representation
        Args:
            string(str): string representation of a list of dictionary
        Return:
            list: The list represented by JSON string
        """
        if json_string is None or len(json_string) == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of attribte set
        Args:
            **dictionary(dict): Double pointer to a dictionary of\
                                key-value pair
        Returns:
            An instance already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            instance = cls(1, 1)
        elif cls is Square:
            instance = cls(1)
        else:
            instance = cls()

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instance from json file
        Return:
            list: A list of an instance
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as json_file:
                json_string = json_file.read()
                list_dicts = Base.from_json_string(json_string)
                instances = []
                for dict_obj in list_dicts:
                    instance = (cls.create(**dict_obj))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
