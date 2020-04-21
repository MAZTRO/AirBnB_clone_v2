#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """ cities """
            objs = models.storage.all()
            list_ob = []
            for key, value in objs.items():
                if 'City' in key and value.state_id == self.id:
                    list_ob.append(value)
            return (list_ob)
