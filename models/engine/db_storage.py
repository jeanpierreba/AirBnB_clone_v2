#!/usr/bin/python3
""" Database storage class """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """ Storage for database with MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_MYSQL_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query on the current database session all objects """
        if cls:
            objs = self.__session.query(self.classes()[cls])
        else:
            objs = self.__session.query(User).all()
            objs += self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Review).all()
        dic = {}
        for obj in objs:
            i = '{}.{}'.format(type(obj).__name__, obj.id)
            dic[i] = obj
        return dic

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """  delete from the current database session
        obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
