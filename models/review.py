#!/usr/bin/python3
"""imports"""
from models.base_model import BaseModel

"""Define Module review"""


class Review(BaseModel):
    """class review"""

    place_id = ""
    user_id = ""
    text = ""
