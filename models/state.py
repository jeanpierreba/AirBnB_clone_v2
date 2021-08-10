#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # relationship between <State> and <City>

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ returns the list of City instances with state_id
            equals to the current State.id """
            all_cities = models.storage.all(City)
            state_city = []
            for city_instance in all_cities.values():
                    if city_instance.state_id == self.id:
                        state_city.append(city_instance)
            return state_city
