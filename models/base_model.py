#!/usr/bin/python3
"""
Imports modules
"""
import uuid
from datetime import datetime
from models import storage

"""
Module that contains class Base
"""


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes instances"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """function str print: [<class name>] (<self.id>) <self.__dict__> """
        className = "[" + self.__class__.__name__ + "]"
        classDict = {
                k: v
                for (k, v) in self.__dict__.items()
                if (not v) is False
        }
        return className + " (" + self.id + ") " + str(classDict)

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        newDict = {}

        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                newDict[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not v:
                    pass
                else:
                    newDict[k] = v
        newDict['__class__'] = self.__class__.__name__

        return newDict
