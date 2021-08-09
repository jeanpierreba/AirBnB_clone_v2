#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # relationship between <State> and <City>
    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan")

    name = ""

    @property
    def cities(self):
        return self.__cities
