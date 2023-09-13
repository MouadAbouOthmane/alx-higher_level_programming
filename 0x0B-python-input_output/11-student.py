#!/usr/bin/python3
"""10. Student to JSON with filter TASK"""


class Student:
    """
    Class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for key in vars(self):
            if key in attrs:
                dic[key] = self.__dict__[key]
        return dic

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            if key in vars(self).keys():
                vars(self)[key] = json[key]
