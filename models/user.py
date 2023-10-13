#!/usr/bin/python3
"""Imports"""

from models.base_model import BaseModel
"""Module user"""


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
