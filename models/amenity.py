#!/usr/bin/python3
""" State Module for HBNB project """
from os import name
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from models.base_model import Base, BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)


    # name = ""
