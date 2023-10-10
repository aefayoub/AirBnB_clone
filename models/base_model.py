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
            self.update_at = datetime.now()
            
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
        #classDict = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return className + " (" + self.id + ") " + self.__dict__
