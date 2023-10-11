#!/usr/bin/python3
"""Imports"""
import json
import os

"""Module FileStorage that serializes instances to a JSON file"""


class Filestorage:
    """class FileStorage that serializes instances to a JSON file """
    __file_path = "file.json"
    __Objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionary = {}

        for k, v in FileStorage.__objects.items():
            dictionary[k] = value.todict()

        with open(FileStorage.__file_path,"w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """Writing the dictionary representation to a file won’t be relevant"""
        from models.base_model import BaseModel

        alldict = {"BaseModel": BaseModel}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FIleStorage.__file_path, "r") as f:
                for k, v in json.load(f).items():
                    self.new(alldict[v["__class__"]](**v)
