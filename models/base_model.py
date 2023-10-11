#!/usr/bin/python3
"""
Imports modules
"""
import uuid
from datetime import datetime

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
            self.update_at = self.created_at
            
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

            self.id = Base.__nb_objects

    def __str__(self):
        """function str print: [<class name>] (<self.id>) <self.__dict__> """
        className = "[" + self.__class__.__name__ + "]"
        classDict = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        classDict = self.__dict__
        return className + " (" + self.id + ") " + str(classDict)

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        #storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        newDict = {}

        for k, v in self.__dict__.items():
            if k == "created_at" or k =="updated_at":
                newDict[k] = v.strftime("")
            else:
                if not v:
                    pass
                else:
                    newDict[k] = v
        newDict["__class__"] = self.__class__.__name__

        return newDict
