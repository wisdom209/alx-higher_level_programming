#!/usr/bin/python3
"""Base python class module"""
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts list_dictionaries to JSON format"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON representation to a file"""
        json_list = []

        if list_objs is not None:
            json_list = [x.to_dictionary() for x in list_objs]

        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as file:
            json.dump(json_list, file)

    @staticmethod
    def from_json_string(json_string):
        """returns list representation of a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes set"""
        from .rectangle import Rectangle
        from .square import Square
        new_cls = None

        if (cls.__name__ == 'Square'):
            new_cls = Square(4, 4, 6)
        elif (cls.__name__ == 'Rectangle'):
            new_cls = Rectangle(2, 4, 6, 8)

        new_cls.update(**dictionary)
        return new_cls

    @classmethod
    def load_from_file(cls):
        """returns a list instance from a file"""
        with open(f"{cls.__name__}.json", mode='r', encoding='utf-8') as file:
            if file is None:
                return []
            my_list_str = file.read()
            my_list = cls.from_json_string(my_list_str)

            return [cls.create(**an_instance_dict)
                    for an_instance_dict in my_list]
