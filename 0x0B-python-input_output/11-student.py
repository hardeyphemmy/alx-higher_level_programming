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


if __name__ == "__main__":

    Student = __import__('11-student').Student
    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').
    load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name,
                            student_1.age))
    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")
    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name,
                            new_student_1.age))
    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name,
                            new_student_1.age))
