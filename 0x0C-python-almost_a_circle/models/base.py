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
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """converts list_dictionaries to JSON format"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
