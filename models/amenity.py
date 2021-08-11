#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.place import place_amenity
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ This class is for amenity attributes """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')
