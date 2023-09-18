#!/usr/bin/python3
"""1. Base class TASK"""
import json


class Base:
    """a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or {}:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """the list of the JSON string representation json_string"""
        if json_string is None or {}:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(10, 10)
        else:
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        filename = cls.__name__ + '.json'
        with open(filename, 'r', encoding="utf-8") as file:
            list_dics = Base.from_json_string(file.read())
            list_objs = []
            for dic in list_dics:
                list_objs.append(cls.create(**dic))
            return list_objs
