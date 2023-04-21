#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import String, Column
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """retutns a list of cities in a state"""
            cities = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
