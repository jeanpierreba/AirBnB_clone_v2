#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Table, Integer, String, ForeignKey, Float

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ This class is for place attributes """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)

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

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place """
            from models.amenity import Amenity
            all_amenities = models.storage.all(Amenity)
            place_amenities = []
            for amenity_instances in all_amenities.values():
                if amenity_instances.place_id == self.id:
                    place_amenities.append(amenity_instances)
            return place_amenities

        @amenities.setter
        def amenities(self, amenity_obj):
            """ handles append method for adding an Amenity.id
            to the attribute amenity_ids """
            if isinstance(amenity_obj, models.Amenity):
                self.amenities.append(amenity_obj.id)
