#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.review import Review
from sqlalchemy.sql.sqltypes import Float
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """ returns the list of Review instances
            with place_id equals to the current Place.id """
            all_reviews = models.storage.all(Review)
            place_review = []
            for review_instances in all_reviews.values():
                if review_instances.place_id == self.id:
                    place_review.append(review_instances)
            return place_review
