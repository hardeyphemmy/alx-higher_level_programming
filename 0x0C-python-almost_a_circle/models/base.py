#!/usr/bin/python3
"""This is a module base."""
import csv
import json
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as cvsfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instance from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                instances = []
                for row in reader:
                    instance = cls.create(**{k: int(v) for k, v in
                                             row.items()})
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """open a window and draw Rectangle and Square"""
        turtle.screen().bgcolour("white")
        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.color("black")
        pen.speed(2)

        for rect in list_rectangles:
            pen.up()
            pen.goto(rect.x, rect.y)
            pen.down()
            for i in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.up()
            pen.goto(square.x, square.y)
            pen.down()
            for i in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()
