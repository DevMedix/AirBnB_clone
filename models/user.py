#!/usr/bin/python3
"""This module contains code for user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class handles all attributes of a user and inheirts
    from the BaseModel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
